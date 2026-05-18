import os
import time
import json
import csv
import re
import requests
import sys
from urllib.parse import unquote
from pathlib import Path

# ------------------------------------------------------------
# 配置
# ------------------------------------------------------------
API_KEY = open("Assets/API.txt", "r").read().strip()  # 从文件读取 API Key
# 北京地域（中国大陆）的异步接口地址
SUBMIT_URL = "https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription"
QUERY_URL_BASE = "https://dashscope.aliyuncs.com/api/v1/tasks/"

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "X-DashScope-Async": "enable",
}

# ------------------------------------------------------------
# 工具函数
# ------------------------------------------------------------
def ms_to_srt_time(ms: int) -> str:
    """将毫秒转换为 SRT 时间格式 HH:MM:SS,mmm"""
    total_sec = ms / 1000.0
    hours = int(total_sec // 3600)
    minutes = int((total_sec % 3600) // 60)
    secs = int(total_sec % 60)
    millis = int(round((total_sec - int(total_sec)) * 1000))
    # 处理毫秒四舍五入导致的进位
    if millis == 1000:
        millis = 0
        secs += 1
        if secs == 60:
            secs = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def sanitize_filename(name: str) -> str:
    """将 object 名称解码并清理为合法的文件夹名"""
    name = unquote(name)
    # 去除扩展名
    if name.endswith(".mp3"):
        name = name[:-4]
    # 替换 Windows 不允许的字符
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    # 压缩连续下划线
    name = re.sub(r"_+", "_", name)
    # 去除首尾下划线或空格
    name = name.strip("_ ")
    return name


# ------------------------------------------------------------
# API 相关函数
# ------------------------------------------------------------
def submit_task(file_url: str) -> str | None:
    """提交异步识别任务，返回 task_id"""
    payload = {
        "model": "qwen3-asr-flash-filetrans",
        "input": {"file_url": file_url},
        "parameters": {
            "enable_itn": True,    # 关闭 ITN，保留原始文本
            "enable_words": True,   # 开启字级时间戳
        },
    }
    resp = requests.post(SUBMIT_URL, headers=HEADERS, json=payload)
    if resp.status_code != 200:
        print(f"  提交任务失败 ({resp.status_code}): {resp.text}")
        return None
    data = resp.json()
    task_id = data.get("output", {}).get("task_id")
    if not task_id:
        print(f"  未获取到 task_id: {data}")
        return None
    return task_id


def poll_task(task_id: str, max_wait_sec: int = 1800) -> dict | None:
    """轮询直到任务完成（默认等待 30 分钟），返回最终的查询响应"""
    start_time = time.time()
    while True:
        time.sleep(2)
        if time.time() - start_time > max_wait_sec:
            print("  任务查询超时")
            return None

        query_url = QUERY_URL_BASE + task_id
        resp = requests.get(query_url, headers=HEADERS)
        if resp.status_code != 200:
            print(f"  查询任务失败 ({resp.status_code}): {resp.text}")
            return None
        data = resp.json()
        status = data.get("output", {}).get("task_status")
        print(f"  任务状态: {status}")
        if status in ("SUCCEEDED", "FAILED", "UNKNOWN"):
            return data


def download_transcription(url: str) -> dict | None:
    """下载识别结果 JSON"""
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"  下载结果失败 ({resp.status_code})")
        return None
    return resp.json()


# ------------------------------------------------------------
# 输出生成函数
# ------------------------------------------------------------
def generate_outputs(base_name: str, result_json: dict, output_dir: Path):
    """根据识别结果生成各种文件"""
    transcripts = result_json.get("transcripts", [])
    if not transcripts:
        print("  没有识别结果，跳过输出")
        return

    # 将所有句子的信息展平
    all_sentences = []
    for trans in transcripts:
        ch = trans.get("channel_id", 0)
        for sent in trans.get("sentences", []):
            sent["channel_id"] = ch
            all_sentences.append(sent)

    # 1. 原始 JSON
    with open(output_dir / f"{base_name}_raw.json", "w", encoding="utf-8") as f:
        json.dump(result_json, f, ensure_ascii=False, indent=2)

    # 2. 纯文本全文
    full_text = "\n".join(s.get("text", "") for s in all_sentences)
    with open(output_dir / f"{base_name}_full.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    # 3. SRT 字幕
    srt_content = ""
    for i, sent in enumerate(all_sentences):
        begin = sent.get("begin_time", 0)
        end = sent.get("end_time", 0)
        text = sent.get("text", "")
        srt_content += f"{i+1}\n"
        srt_content += f"{ms_to_srt_time(begin)} --> {ms_to_srt_time(end)}\n"
        srt_content += f"{text}\n\n"
    with open(output_dir / f"{base_name}.srt", "w", encoding="utf-8") as f:
        f.write(srt_content)

    # 4. 字级时间戳 JSON
    words_list = []
    for sent in all_sentences:
        for w in sent.get("words", []):
            w_copy = dict(w)
            w_copy["sentence_id"] = sent["sentence_id"]
            words_list.append(w_copy)
    if words_list:
        with open(output_dir / f"{base_name}_words.json", "w", encoding="utf-8") as f:
            json.dump(words_list, f, ensure_ascii=False, indent=2)

    # 5. 情感信息 JSON
    emotions = []
    for sent in all_sentences:
        emotions.append({
            "sentence_id": sent["sentence_id"],
            "text": sent.get("text", ""),
            "language": sent.get("language", ""),
            "emotion": sent.get("emotion", ""),
        })
    with open(output_dir / f"{base_name}_emotion.json", "w", encoding="utf-8") as f:
        json.dump(emotions, f, ensure_ascii=False, indent=2)

    # 6. 带时间戳的文本
    lines = []
    for sent in all_sentences:
        begin = ms_to_srt_time(sent["begin_time"]).replace(",", ".")
        end = ms_to_srt_time(sent["end_time"]).replace(",", ".")
        text = sent["text"]
        lines.append(f"[{begin} - {end}] {text}")
    with open(output_dir / f"{base_name}_timestamps.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"  已生成 6 种识别文件 -> {output_dir}")


# ------------------------------------------------------------
# 主流程
# ------------------------------------------------------------
def process_row(row: dict):
    obj = row["object"]
    url = row["url"]
    print(f"\n===== 开始处理: {obj} =====")

    base_name = sanitize_filename(obj)
    sub_dir = OUTPUT_DIR / base_name
    sub_dir.mkdir(parents=True, exist_ok=True)

    # 1. 提交任务
    task_id = submit_task(url)
    if not task_id:
        return
    print(f"  task_id: {task_id}")

    # 2. 等待任务完成
    final_resp = poll_task(task_id)
    if not final_resp:
        print(f"  任务未能完成，跳过 {obj}")
        return

    status = final_resp["output"]["task_status"]
    if status != "SUCCEEDED":
        msg = final_resp["output"].get("message", "")
        print(f"  任务失败: {msg}")
        # 保存错误信息供排查
        with open(sub_dir / "error.json", "w", encoding="utf-8") as f:
            json.dump(final_resp, f, ensure_ascii=False, indent=2)
        return

    # 3. 下载识别结果
    result_url = final_resp["output"].get("result", {}).get("transcription_url")
    if not result_url:
        print("  未找到 transcription_url")
        return
    print("  下载识别结果中...")
    result_json = download_transcription(result_url)
    if not result_json:
        return

    # 4. 生成各类输出文件
    generate_outputs(base_name, result_json, sub_dir)
    print(f"  ✓ 完成 {obj}")


def main():
    # 读取 CSV
    try:
        with open("Code/urls.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        print("错误: 找不到 urls.csv 文件，请放在当前路径下。")
        sys.exit(1)

    print(f"共发现 {len(rows)} 个音频文件，开始处理...")

    for idx, row in enumerate(rows):
        print(f"\n{'='*50}\n进度: {idx+1}/{len(rows)}")
        try:
            process_row(row)
        except Exception as e:
            print(f"处理 {row.get('object', 'unknown')} 时发生异常: {e}")

    print("\n所有文件处理完毕，输出保存在 'output/' 目录下。")


if __name__ == "__main__":
    main()