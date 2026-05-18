# 录音文件识别-千问

千问系列的录音文件识别模型能将录制好的音频转换为文本，支持多语言识别、歌唱识别、噪声拒识等功能。

## **核心功能**

-   **多语种识别：**支持多语种语音识别（涵盖普通话及多种方言，如粤语、四川话等）。
    
-   **复杂环境适应：**具备应对复杂声学环境的能力，支持自动语种检测与智能非人声过滤。
    
-   **歌唱识别：**即使在伴随背景音乐（BGM）的情况下，也能实现整首歌曲的转写。
    
-   **情感识别：**支持多种情绪状态识别（涵盖惊讶、平静、愉快、悲伤、厌恶、愤怒和恐惧）。
    

## **适用范围**

**支持的模型：**

服务主要提供两大核心模型：

-   **千问3-ASR-Flash-Filetrans**：专为长音频（最长12小时）的异步识别设计，适用于会议记录、访谈整理等场景。
    
-   **千问3-ASR-Flash**：专为短音频（最长5分钟）的同步或流式识别设计，适用于语音消息、实时字幕等场景。
    

## 中国内地

服务部署范围为[中国内地](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**北京接入地域**，模型推理计算资源仅限于中国内地。

调用以下模型时，请选择北京地域的[API Key](https://bailian.console.aliyun.com/?tab=model#/api-key)：

-   **千问3-ASR-Flash-Filetrans：**qwen3-asr-flash-filetrans（稳定版，当前等同qwen3-asr-flash-filetrans-2025-11-17）、qwen3-asr-flash-filetrans-2025-11-17（快照版）
    
-   **千问3-ASR-Flash：**qwen3-asr-flash（稳定版，当前等同qwen3-asr-flash-2025-09-08）、qwen3-asr-flash-2026-02-10（最新快照版）、qwen3-asr-flash-2025-09-08（快照版）
    

## 国际

服务部署范围为[国际](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**新加坡接入地域**，模型推理计算资源在全球范围内动态调度（不含中国内地）。

调用以下模型时，请选择新加坡地域的[API Key](https://modelstudio.console.aliyun.com/?tab=dashboard#/api-key)：

-   **千问3-ASR-Flash-Filetrans：**qwen3-asr-flash-filetrans（稳定版，当前等同qwen3-asr-flash-filetrans-2025-11-17）、qwen3-asr-flash-filetrans-2025-11-17（快照版）
    
-   **千问3-ASR-Flash：**qwen3-asr-flash（稳定版，当前等同qwen3-asr-flash-2025-09-08）、qwen3-asr-flash-2026-02-10（最新快照版）、qwen3-asr-flash-2025-09-08（快照版）
    

## 美国

服务部署范围为[美国](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**美国（弗吉尼亚）接入地域**，模型推理计算资源仅限于美国境内。

调用以下模型时，请选择美国地域的[API Key](https://modelstudio.console.aliyun.com/us-east-1?tab=dashboard#/api-key)：

**千问3-ASR-Flash：**qwen3-asr-flash-us（稳定版，当前等同qwen3-asr-flash-2025-09-08-us）、qwen3-asr-flash-2025-09-08-us（快照版）

## **模型选型**

| **场景** | **推荐模型** | **理由** | **注意事项** |
| --- | --- | --- | --- |
| **长音频识别** | qwen3-asr-flash-filetrans | 支持最长12小时录音，具备情感识别与句/字级别时间戳功能，适合后期索引与分析 | 音频文件大小不超过2GB，且时长不超过12小时 |
| **短音频识别** | qwen3-asr-flash或qwen3-asr-flash-us | 短音频识别，低延迟 | 音频文件大小不超过10MB，且时长不超过5分钟 |
| **客服质检** | qwen3-asr-flash-filetrans、qwen3-asr-flash或qwen3-asr-flash-us | 可分析客户情绪 | 不支持敏感词过滤；无说话人分离；根据音频时长选择合适的模型 |
| **新闻/访谈节目字幕生成** | qwen3-asr-flash-filetrans | 长音频+标点预测+时间戳，直接生成结构化字幕 | 需后处理生成标准字幕文件；根据音频时长选择合适的模型 |
| **多语种视频本地化** | qwen3-asr-flash-filetrans、qwen3-asr-flash或qwen3-asr-flash-us | 覆盖多种语言+方言，适合跨语种字幕制作 | 根据音频时长选择合适的模型 |
| **歌唱类音频分析** | qwen3-asr-flash-filetrans、qwen3-asr-flash或qwen3-asr-flash-us | 识别歌词并分析情绪，适用于歌曲索引与推荐 | 根据音频时长选择合适的模型 |

更多说明请参见[模型功能特性对比](#ea5edc7ae4cq7)。

## **快速开始**

API 使用前提：已[获取API Key](https://help.aliyun.com/zh/model-studio/get-api-key)。如果通过SDK调用，需要[安装最新版SDK](https://help.aliyun.com/zh/model-studio/install-sdk#8833b9274f4v8)。

## DashScope

## 千问3-ASR-Flash-Filetrans

千问3-ASR-Flash-Filetrans模型专为音频文件的异步转写设计，支持最长12小时录音。该模型要求输入为公网可访问的音频文件URL，不支持直接上传本地文件。此外，它是一个非流式接口，会在任务完成后一次性返回全部识别结果。

## cURL

使用 cURL 进行语音识别时，需先提交任务获取任务ID（task\_id），再通过该ID获取任务执行结果。

## 提交任务

```
# ======= 重要提示 =======
# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/audio/asr/transcription
# 新加坡地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
# === 执行时请删除该注释 ===

curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription' \
-H "Authorization: Bearer $DASHSCOPE_API_KEY" \
-H "Content-Type: application/json" \
-H "X-DashScope-Async: enable" \
-d '{
    "model": "qwen3-asr-flash-filetrans",
    "input": {
        "file_url": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
    },
    "parameters": {
        "channel_id":[
            0
        ],
        "enable_itn": false,
        "enable_words": true
    }
}'
```

## 获取任务执行结果

```
# ======= 重要提示 =======
# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/tasks/{task_id}，注意，将{task_id}替换为待查询任务ID
# 新加坡地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
# === 执行时请删除该注释 ===

curl -X GET 'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}' \
-H "Authorization: Bearer $DASHSCOPE_API_KEY" \
-H "X-DashScope-Async: enable" \
-H "Content-Type: application/json"
```

## 完整示例

## Java

```
import com.google.gson.Gson;
import com.google.gson.annotations.SerializedName;
import okhttp3.*;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class Main {
    // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/audio/asr/transcription
    private static final String API_URL_SUBMIT = "https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription";
    // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/tasks/
    private static final String API_URL_QUERY = "https://dashscope.aliyuncs.com/api/v1/tasks/";
    private static final Gson gson = new Gson();

    public static void main(String[] args) {
        // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
        // 若没有配置环境变量，请用百炼API Key将下行替换为：String apiKey = "sk-xxx"
        String apiKey = System.getenv("DASHSCOPE_API_KEY");

        OkHttpClient client = new OkHttpClient();

        // 1. 提交任务
        /*String payloadJson = """
                {
                    "model": "qwen3-asr-flash-filetrans",
                    "input": {
                        "file_url": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
                    },
                    "parameters": {
                        "channel_id": [0],
                        "enable_itn": false,
                        "language": "zh"
                    }
                }
                """;*/
        String payloadJson = """
                {
                    "model": "qwen3-asr-flash-filetrans",
                    "input": {
                        "file_url": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
                    },
                    "parameters": {
                        "channel_id": [0],
                        "enable_itn": false,
                        "enable_words": true
                    }
                }
                """;

        RequestBody body = RequestBody.create(payloadJson, MediaType.get("application/json; charset=utf-8"));
        Request submitRequest = new Request.Builder()
                .url(API_URL_SUBMIT)
                .addHeader("Authorization", "Bearer " + apiKey)
                .addHeader("Content-Type", "application/json")
                .addHeader("X-DashScope-Async", "enable")
                .post(body)
                .build();

        String taskId = null;

        try (Response response = client.newCall(submitRequest).execute()) {
            if (response.isSuccessful() && response.body() != null) {
                String respBody = response.body().string();
                ApiResponse apiResp = gson.fromJson(respBody, ApiResponse.class);
                if (apiResp.output != null) {
                    taskId = apiResp.output.taskId;
                    System.out.println("任务已提交，task_id: " + taskId);
                } else {
                    System.out.println("提交返回内容: " + respBody);
                    return;
                }
            } else {
                System.out.println("任务提交失败! HTTP code: " + response.code());
                if (response.body() != null) {
                    System.out.println(response.body().string());
                }
                return;
            }
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }

        // 2. 轮询任务状态
        boolean finished = false;
        while (!finished) {
            try {
                TimeUnit.SECONDS.sleep(2);  // 等待 2 秒再查询
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                return;
            }

            String queryUrl = API_URL_QUERY + taskId;
            Request queryRequest = new Request.Builder()
                    .url(queryUrl)
                    .addHeader("Authorization", "Bearer " + apiKey)
                    .addHeader("X-DashScope-Async", "enable")
                    .addHeader("Content-Type", "application/json")
                    .get()
                    .build();

            try (Response response = client.newCall(queryRequest).execute()) {
                if (response.body() != null) {
                    String queryResponse = response.body().string();
                    ApiResponse apiResp = gson.fromJson(queryResponse, ApiResponse.class);

                    if (apiResp.output != null && apiResp.output.taskStatus != null) {
                        String status = apiResp.output.taskStatus;
                        System.out.println("当前任务状态: " + status);
                        if ("SUCCEEDED".equalsIgnoreCase(status)
                                || "FAILED".equalsIgnoreCase(status)
                                || "UNKNOWN".equalsIgnoreCase(status)) {
                            finished = true;
                            System.out.println("任务完成，最终结果: ");
                            System.out.println(queryResponse);
                        }
                    } else {
                        System.out.println("查询返回内容: " + queryResponse);
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
                return;
            }
        }
    }

    static class ApiResponse {
        @SerializedName("request_id")
        String requestId;
        Output output;
    }

    static class Output {
        @SerializedName("task_id")
        String taskId;
        @SerializedName("task_status")
        String taskStatus;
    }
}
```

## Python

```
import os
import time
import requests
import json

# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/audio/asr/transcription
API_URL_SUBMIT = "https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription"
# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/tasks/
API_URL_QUERY_BASE = "https://dashscope.aliyuncs.com/api/v1/tasks/"


def main():
    # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx"
    api_key = os.getenv("DASHSCOPE_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable"
    }

    # 1. 提交任务
    payload = {
        "model": "qwen3-asr-flash-filetrans",
        "input": {
            "file_url": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
        },
        "parameters": {
            "channel_id": [0],
            # "language": "zh",
            "enable_itn": False,
            "enable_words": True
        }
    }

    print("提交 ASR 转写任务...")
    try:
        submit_resp = requests.post(API_URL_SUBMIT, headers=headers, data=json.dumps(payload))
    except requests.RequestException as e:
        print(f"请求提交任务失败: {e}")
        return

    if submit_resp.status_code != 200:
        print(f"任务提交失败! HTTP code: {submit_resp.status_code}")
        print(submit_resp.text)
        return

    resp_data = submit_resp.json()
    output = resp_data.get("output")
    if not output or "task_id" not in output:
        print("提交返回内容异常:", resp_data)
        return

    task_id = output["task_id"]
    print(f"任务已提交，task_id: {task_id}")

    # 2. 轮询任务状态
    finished = False
    while not finished:
        time.sleep(2)  # 等待 2 秒再查询

        query_url = API_URL_QUERY_BASE + task_id
        try:
            query_resp = requests.get(query_url, headers=headers)
        except requests.RequestException as e:
            print(f"请求查询任务失败: {e}")
            return

        if query_resp.status_code != 200:
            print(f"查询任务失败! HTTP code: {query_resp.status_code}")
            print(query_resp.text)
            return

        query_data = query_resp.json()
        output = query_data.get("output")
        if output and "task_status" in output:
            status = output["task_status"]
            print(f"当前任务状态: {status}")

            if status.upper() in ("SUCCEEDED", "FAILED", "UNKNOWN"):
                finished = True
                print("任务完成，最终结果如下：")
                print(json.dumps(query_data, indent=2, ensure_ascii=False))
        else:
            print("查询返回内容:", query_data)


if __name__ == "__main__":
    main()
```

## Java SDK

```
import com.alibaba.dashscope.audio.qwen_asr.*;
import com.alibaba.dashscope.utils.Constants;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1
        Constants.baseHttpApiUrl = "https://dashscope.aliyuncs.com/api/v1";
        QwenTranscriptionParam param =
                QwenTranscriptionParam.builder()
                        // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
                        // 若没有配置环境变量，请用百炼API Key将下行替换为：.apiKey("sk-xxx")
                        .apiKey(System.getenv("DASHSCOPE_API_KEY"))
                        .model("qwen3-asr-flash-filetrans")
                        .fileUrl("https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/sensevoice/rich_text_example_1.wav")
                        //.parameter("language", "zh")
                        //.parameter("channel_id", new ArrayList<String>(){{add("0");add("1");}})
                        .parameter("enable_itn", false)
                        .parameter("enable_words", true)
                        .build();
        try {
            QwenTranscription transcription = new QwenTranscription();
            // 提交任务
            QwenTranscriptionResult result = transcription.asyncCall(param);
            System.out.println("create task result: " + result);
            // 查询任务状态
            result = transcription.fetch(QwenTranscriptionQueryParam.FromTranscriptionParam(param, result.getTaskId()));
            System.out.println("task status: " + result);
            // 等待任务完成
            result =
                    transcription.wait(
                            QwenTranscriptionQueryParam.FromTranscriptionParam(param, result.getTaskId()));
            System.out.println("task result: " + result);
            // 获取语音识别结果
            QwenTranscriptionTaskResult taskResult = result.getResult();
            if (taskResult != null) {
                // 获取识别结果的url
                String transcriptionUrl = taskResult.getTranscriptionUrl();
                // 获取url内对应的结果
                HttpURLConnection connection =
                        (HttpURLConnection) new URL(transcriptionUrl).openConnection();
                connection.setRequestMethod("GET");
                connection.connect();
                BufferedReader reader =
                        new BufferedReader(new InputStreamReader(connection.getInputStream()));
                // 格式化输出json结果
                Gson gson = new GsonBuilder().setPrettyPrinting().create();
                System.out.println(gson.toJson(gson.fromJson(reader, JsonObject.class)));
            }
        } catch (Exception e) {
            System.out.println("error: " + e);
        }
    }
}
```

## Python SDK

```
import json
import os
import sys
from http import HTTPStatus

import dashscope
from dashscope.audio.qwen_asr import QwenTranscription
from dashscope.api_entities.dashscope_response import TranscriptionResponse


# run the transcription script
if __name__ == '__main__':
    # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    # 若没有配置环境变量，请用百炼API Key将下行替换为：dashscope.api_key = "sk-xxx"
    dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")

    # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1
    dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'
    task_response = QwenTranscription.async_call(
        model='qwen3-asr-flash-filetrans',
        file_url='https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/sensevoice/rich_text_example_1.wav',
        #language="",
        enable_itn=False,
        enable_words=True
    )
    print(f'task_response: {task_response}')
    print(task_response.output.task_id)
    query_response = QwenTranscription.fetch(task=task_response.output.task_id)
    print(f'query_response: {query_response}')
    task_result = QwenTranscription.wait(task=task_response.output.task_id)
    print(f'task_result: {task_result}')
```

## 千问3-ASR-Flash

千问3-ASR-Flash模型支持最长5分钟录音。该模型可输入公网可访问的音频文件URL或直接上传本地文件。此外，它可流式返回识别结果。

## 输入内容：音频文件URL

## Python SDK

```
import os
import dashscope

# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

messages = [
    {"role": "user", "content": [{"audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"}]}
]

response = dashscope.MultiModalConversation.call(
    # 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    # 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us
    model="qwen3-asr-flash",
    messages=messages,
    result_format="message",
    asr_options={
        # "language": "zh", # 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        "enable_itn":False
    }
)
print(response)
```

## Java SDK

```
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversation;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationParam;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationResult;
import com.alibaba.dashscope.common.MultiModalMessage;
import com.alibaba.dashscope.common.Role;
import com.alibaba.dashscope.exception.ApiException;
import com.alibaba.dashscope.exception.NoApiKeyException;
import com.alibaba.dashscope.exception.UploadFileException;
import com.alibaba.dashscope.utils.Constants;
import com.alibaba.dashscope.utils.JsonUtils;

public class Main {
    public static void simpleMultiModalConversationCall()
            throws ApiException, NoApiKeyException, UploadFileException {
        MultiModalConversation conv = new MultiModalConversation();
        MultiModalMessage userMessage = MultiModalMessage.builder()
                .role(Role.USER.getValue())
                .content(Arrays.asList(
                        Collections.singletonMap("audio", "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3")))
                .build();

        Map<String, Object> asrOptions = new HashMap<>();
        asrOptions.put("enable_itn", false);
        // asrOptions.put("language", "zh"); // 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        MultiModalConversationParam param = MultiModalConversationParam.builder()
                // 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
                // 若没有配置环境变量，请用百炼API Key将下行替换为：.apiKey("sk-xxx")
                .apiKey(System.getenv("DASHSCOPE_API_KEY"))
                // 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us
                .model("qwen3-asr-flash")
                .message(userMessage)
                .parameter("asr_options", asrOptions)
                .build();
        MultiModalConversationResult result = conv.call(param);
        System.out.println(JsonUtils.toJson(result));
    }
    public static void main(String[] args) {
        try {
            // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1
            Constants.baseHttpApiUrl = "https://dashscope.aliyuncs.com/api/v1";
            simpleMultiModalConversationCall();
        } catch (ApiException | NoApiKeyException | UploadFileException e) {
            System.out.println(e.getMessage());
        }
        System.exit(0);
    }
}
```

## cURL

```
# ======= 重要提示 =======
# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation
# 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
# 若使用美国地域的模型，需要加us后缀
# === 执行时请删除该注释 ===

curl -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation" \
-H "Authorization: Bearer $DASHSCOPE_API_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "qwen3-asr-flash",
    "input": {
        "messages": [
            {
                "content": [
                    {
                        "text": ""
                    }
                ],
                "role": "system"
            },
            {
                "content": [
                    {
                        "audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
                    }
                ],
                "role": "user"
            }
        ]
    },
    "parameters": {
        "asr_options": {
            "enable_itn": false
        }
    }
}'
```

## 输入内容：Base64编码的音频文件

可输入Base64编码数据（[Data URL](https://www.rfc-editor.org/rfc/rfc2397)），格式为：`data:<mediatype>;base64,<data>`。

-   `<mediatype>`：MIME类型
    
    因音频格式而异，例如：
    
    -   WAV：`audio/wav`
        
    -   MP3：`audio/mpeg`
        
-   `<data>`：音频转成的Base64编码的字符串
    
    Base64编码会增大体积，请控制原文件大小，确保编码后仍符合输入音频大小限制（10MB）
    
-   示例：`data:audio/wav;base64,SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4LjI5LjEwMAAAAAAAAAAAAAAA//PAxABQ/BXRbMPe4IQAhl9`
    
    **点击查看示例代码**
    
    Python
    
    ```
    import base64, pathlib
    
    # input.mp3为用于声音复刻的本地音频文件，请替换为自己的音频文件路径，确保其符合音频要求
    file_path = pathlib.Path("input.mp3")
    base64_str = base64.b64encode(file_path.read_bytes()).decode()
    data_uri = f"data:audio/mpeg;base64,{base64_str}"
    ```
    
    Java
    
    ```
    import java.nio.file.*;
    import java.util.Base64;
    
    public class Main {
        /**
         * filePath为用于声音复刻的本地音频文件，请替换为自己的音频文件路径，确保其符合音频要求
         */
        public static String toDataUrl(String filePath) throws Exception {
            byte[] bytes = Files.readAllBytes(Paths.get(filePath));
            String encoded = Base64.getEncoder().encodeToString(bytes);
            return "data:audio/mpeg;base64," + encoded;
        }
    
        // 使用示例
        public static void main(String[] args) throws Exception {
            System.out.println(toDataUrl("input.mp3"));
        }
    }
    ```
    

## Python SDK

示例中用到的音频文件为：[welcome.mp3](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260105/wotsae/welcome.mp3)。

```
import base64
import dashscope
import os
import pathlib

# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

# 请替换为实际的音频文件路径
file_path = "welcome.mp3"
# 请替换为实际的音频文件MIME类型
audio_mime_type = "audio/mpeg"

file_path_obj = pathlib.Path(file_path)
if not file_path_obj.exists():
    raise FileNotFoundError(f"音频文件不存在: {file_path}")

base64_str = base64.b64encode(file_path_obj.read_bytes()).decode()
data_uri = f"data:{audio_mime_type};base64,{base64_str}"

messages = [
    {"role": "user", "content": [{"audio": data_uri}]}
]
response = dashscope.MultiModalConversation.call(
    # 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    # 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us
    model="qwen3-asr-flash",
    messages=messages,
    result_format="message",
    asr_options={
        # "language": "zh", # 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        "enable_itn":False
    }
)
print(response)
```

## Java SDK

示例中用到的音频文件为：[welcome.mp3](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260105/wotsae/welcome.mp3)。

```
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversation;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationParam;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationResult;
import com.alibaba.dashscope.common.MultiModalMessage;
import com.alibaba.dashscope.common.Role;
import com.alibaba.dashscope.exception.ApiException;
import com.alibaba.dashscope.exception.NoApiKeyException;
import com.alibaba.dashscope.exception.UploadFileException;
import com.alibaba.dashscope.utils.Constants;
import com.alibaba.dashscope.utils.JsonUtils;

public class Main {
    // 请替换为实际的音频文件路径
    private static final String AUDIO_FILE = "welcome.mp3";
    // 请替换为实际的音频文件MIME类型
    private static final String AUDIO_MIME_TYPE = "audio/mpeg";

    public static void simpleMultiModalConversationCall()
            throws ApiException, NoApiKeyException, UploadFileException, IOException {
        MultiModalConversation conv = new MultiModalConversation();
        MultiModalMessage userMessage = MultiModalMessage.builder()
                .role(Role.USER.getValue())
                .content(Arrays.asList(
                        Collections.singletonMap("audio", toDataUrl())))
                .build();

        Map<String, Object> asrOptions = new HashMap<>();
        asrOptions.put("enable_itn", false);
        // asrOptions.put("language", "zh"); // 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        MultiModalConversationParam param = MultiModalConversationParam.builder()
                // 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
                // 若没有配置环境变量，请用百炼API Key将下行替换为：.apiKey("sk-xxx")
                .apiKey(System.getenv("DASHSCOPE_API_KEY"))
                // 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us
                .model("qwen3-asr-flash")
                .message(userMessage)
                .parameter("asr_options", asrOptions)
                .build();
        MultiModalConversationResult result = conv.call(param);
        System.out.println(JsonUtils.toJson(result));
    }

    public static void main(String[] args) {
        try {
            // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1
            Constants.baseHttpApiUrl = "https://dashscope.aliyuncs.com/api/v1";
            simpleMultiModalConversationCall();
        } catch (ApiException | NoApiKeyException | UploadFileException | IOException e) {
            System.out.println(e.getMessage());
        }
        System.exit(0);
    }

    // 生成 data URI
    public static String toDataUrl() throws IOException {
        byte[] bytes = Files.readAllBytes(Paths.get(AUDIO_FILE));
        String encoded = Base64.getEncoder().encodeToString(bytes);
        return "data:" + AUDIO_MIME_TYPE + ";base64," + encoded;
    }
}
```

## 输入内容：本地音频文件绝对路径

使用DashScope SDK处理本地图像文件时，需要传入文件路径。请您参考下表，结合您的使用方式与操作系统进行文件路径的创建。

| **系统** | **SDK** | **传入的文件路径** | **示例** |
| --- | --- | --- | --- |
| Linux或macOS系统 | Python SDK | file://{文件的绝对路径} | file:///home/images/test.png |
| Java SDK |
| Windows系统 | Python SDK | file://{文件的绝对路径} | file://D:/images/test.png |
| Java SDK | file:///{文件的绝对路径} | file:///D:images/test.png |

**重要**

使用本地文件时，接口调用上限为 100 QPS，且不支持扩容，请勿用于生产环境、高并发及压测场景；如需更高并发，建议将文件上传至 OSS 并通过录音文件 URL 方式调用。

## Python SDK

示例中用到的音频文件为：[welcome.mp3](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260105/wotsae/welcome.mp3)。

```
import os
import dashscope

# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

# 请用您的本地音频的绝对路径替换 ABSOLUTE_PATH/welcome.mp3
audio_file_path = "file://ABSOLUTE_PATH/welcome.mp3"

messages = [
    {"role": "user", "content": [{"audio": audio_file_path}]}
]
response = dashscope.MultiModalConversation.call(
    # 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    # 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us
    model="qwen3-asr-flash",
    messages=messages,
    result_format="message",
    asr_options={
        # "language": "zh", # 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        "enable_itn":False
    }
)
print(response)
```

## Java SDK

示例中用到的音频文件为：[welcome.mp3](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260105/wotsae/welcome.mp3)。

```
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversation;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationParam;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationResult;
import com.alibaba.dashscope.common.MultiModalMessage;
import com.alibaba.dashscope.common.Role;
import com.alibaba.dashscope.exception.ApiException;
import com.alibaba.dashscope.exception.NoApiKeyException;
import com.alibaba.dashscope.exception.UploadFileException;
import com.alibaba.dashscope.utils.Constants;
import com.alibaba.dashscope.utils.JsonUtils;

public class Main {
    public static void simpleMultiModalConversationCall()
            throws ApiException, NoApiKeyException, UploadFileException {
        // 请用您本地文件的绝对路径替换掉ABSOLUTE_PATH/welcome.mp3
        String localFilePath = "file://ABSOLUTE_PATH/welcome.mp3";
        MultiModalConversation conv = new MultiModalConversation();
        MultiModalMessage userMessage = MultiModalMessage.builder()
                .role(Role.USER.getValue())
                .content(Arrays.asList(
                        Collections.singletonMap("audio", localFilePath)))
                .build();

        Map<String, Object> asrOptions = new HashMap<>();
        asrOptions.put("enable_itn", false);
        // asrOptions.put("language", "zh"); // 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        MultiModalConversationParam param = MultiModalConversationParam.builder()
                // 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
                // 若没有配置环境变量，请用百炼API Key将下行替换为：.apiKey("sk-xxx")
                .apiKey(System.getenv("DASHSCOPE_API_KEY"))
                // 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us
                .model("qwen3-asr-flash")
                .message(userMessage)
                .parameter("asr_options", asrOptions)
                .build();
        MultiModalConversationResult result = conv.call(param);
        System.out.println(JsonUtils.toJson(result));
    }
    public static void main(String[] args) {
        try {
            // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1
            Constants.baseHttpApiUrl = "https://dashscope.aliyuncs.com/api/v1";
            simpleMultiModalConversationCall();
        } catch (ApiException | NoApiKeyException | UploadFileException e) {
            System.out.println(e.getMessage());
        }
        System.exit(0);
    }
}
```

## 流式输出

模型并不是一次性生成最终结果，而是逐步地生成中间结果，最终结果由中间结果拼接而成。使用非流式输出方式需要等待模型生成结束后再将生成的中间结果拼接后返回，而流式输出可以实时地将中间结果返回，您可以在模型进行输出的同时进行阅读，减少等待模型回复的时间。您可以根据调用方式来设置不同的参数以实现流式输出：

-   DashScope Python SDK方式：设置`stream`参数为true。
    
-   DashScope Java SDK方式：需要通过`streamCall`接口调用。
    
-   DashScope HTTP方式：需要在Header中指定`X-DashScope-SSE`为`enable`。
    

## Python SDK

```
import os
import dashscope

# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

messages = [
    {"role": "user", "content": [{"audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"}]}
]
response = dashscope.MultiModalConversation.call(
    # 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    # 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us
    model="qwen3-asr-flash",
    messages=messages,
    result_format="message",
    asr_options={
        # "language": "zh", # 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        "enable_itn":False
    },
    stream=True
)

for response in response:
    try:
        print(response["output"]["choices"][0]["message"].content[0]["text"])
    except:
        pass
```

## Java SDK

```
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversation;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationParam;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationResult;
import com.alibaba.dashscope.common.MultiModalMessage;
import com.alibaba.dashscope.common.Role;
import com.alibaba.dashscope.exception.ApiException;
import com.alibaba.dashscope.exception.NoApiKeyException;
import com.alibaba.dashscope.exception.UploadFileException;
import com.alibaba.dashscope.utils.Constants;
import io.reactivex.Flowable;

public class Main {
    public static void simpleMultiModalConversationCall()
            throws ApiException, NoApiKeyException, UploadFileException {
        MultiModalConversation conv = new MultiModalConversation();
        MultiModalMessage userMessage = MultiModalMessage.builder()
                .role(Role.USER.getValue())
                .content(Arrays.asList(
                        Collections.singletonMap("audio", "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3")))
                .build();

        Map<String, Object> asrOptions = new HashMap<>();
        asrOptions.put("enable_itn", false);
        // asrOptions.put("language", "zh"); // 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        MultiModalConversationParam param = MultiModalConversationParam.builder()
                // 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
                // 若没有配置环境变量，请用百炼API Key将下行替换为：.apiKey("sk-xxx")
                .apiKey(System.getenv("DASHSCOPE_API_KEY"))
                // 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us
                .model("qwen3-asr-flash")
                .message(userMessage)
                .parameter("asr_options", asrOptions)
                .build();
        Flowable<MultiModalConversationResult> resultFlowable = conv.streamCall(param);
        resultFlowable.blockingForEach(item -> {
            try {
                System.out.println(item.getOutput().getChoices().get(0).getMessage().getContent().get(0).get("text"));
            } catch (Exception e){
                System.exit(0);
            }
        });
    }

    public static void main(String[] args) {
        try {
            // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1
            Constants.baseHttpApiUrl = "https://dashscope.aliyuncs.com/api/v1";
            simpleMultiModalConversationCall();
        } catch (ApiException | NoApiKeyException | UploadFileException e) {
            System.out.println(e.getMessage());
        }
        System.exit(0);
    }
}
```

## cURL

```
# ======= 重要提示 =======
# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation
# 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
# 若使用美国地域的模型，需要加us后缀
# === 执行时请删除该注释 ===

curl -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation" \
-H "Authorization: Bearer $DASHSCOPE_API_KEY" \
-H "Content-Type: application/json" \
-H "X-DashScope-SSE: enable" \
-d '{
    "model": "qwen3-asr-flash",
    "input": {
        "messages": [
            {
                "content": [
                    {
                        "text": ""
                    }
                ],
                "role": "system"
            },
            {
                "content": [
                    {
                        "audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
                    }
                ],
                "role": "user"
            }
        ]
    },
    "parameters": {
        "incremental_output": true,
        "asr_options": {
            "enable_itn": false
        }
    }
}'
```

## OpenAI兼容

仅千问3-ASR-Flash系列模型支持OpenAI兼容方式调用。OpenAI兼容方式仅允许输入公网可访问的音频文件URL，不支持输入本地音频文件绝对路径。

OpenAI Python SDK 版本应不低于1.52.0， Node.js SDK 版本应不低于 4.68.0。

`asr_options`非OpenAI标准参数，若使用OpenAI SDK，请通过`extra_body`传入。

## 输入内容：音频文件URL

## Python SDK

```
from openai import OpenAI
import os

try:
    client = OpenAI(
        # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    

    stream_enabled = False  # 是否开启流式输出
    completion = client.chat.completions.create(
        model="qwen3-asr-flash",
        messages=[
            {
                "content": [
                    {
                        "type": "input_audio",
                        "input_audio": {
                            "data": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
                        }
                    }
                ],
                "role": "user"
            }
        ],
        stream=stream_enabled,
        # stream设为False时，不能设置stream_options参数
        # stream_options={"include_usage": True},
        extra_body={
            "asr_options": {
                # "language": "zh",
                "enable_itn": False
            }
        }
    )
    if stream_enabled:
        full_content = ""
        print("流式输出内容为：")
        for chunk in completion:
            # 如果stream_options.include_usage为True，则最后一个chunk的choices字段为空列表，需要跳过（可以通过chunk.usage获取 Token 使用量）
            print(chunk)
            if chunk.choices and chunk.choices[0].delta.content:
                full_content += chunk.choices[0].delta.content
        print(f"完整内容为：{full_content}")
    else:
        print(f"非流式输出内容为：{completion.choices[0].message.content}")
except Exception as e:
    print(f"错误信息：{e}")
```

## Node.js SDK

```
// 运行前的准备工作:
// Windows/Mac/Linux 通用:
// 1. 确保已安装 Node.js (建议版本 >= 14)
// 2. 运行以下命令安装必要的依赖: npm install openai

import OpenAI from "openai";

const client = new OpenAI({
  // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
  // 若没有配置环境变量，请用百炼API Key将下行替换为：apiKey: "sk-xxx",
  apiKey: process.env.DASHSCOPE_API_KEY,
  // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
  baseURL: "https://dashscope.aliyuncs.com/compatible-mode/v1", 
});

async function main() {
  try {
    const streamEnabled = false; // 是否开启流式输出
    const completion = await client.chat.completions.create({
      model: "qwen3-asr-flash",
      messages: [
        {
          role: "user",
          content: [
            {
              type: "input_audio",
              input_audio: {
                data: "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
              }
            }
          ]
        }
      ],
      stream: streamEnabled,
      // stream设为False时，不能设置stream_options参数
      // stream_options: {
      //   "include_usage": true
      // },
      extra_body: {
        asr_options: {
          // language: "zh",
          enable_itn: false
        }
      }
    });

    if (streamEnabled) {
      let fullContent = "";
      console.log("流式输出内容为：");
      for await (const chunk of completion) {
        console.log(JSON.stringify(chunk));
        if (chunk.choices && chunk.choices.length > 0) {
          const delta = chunk.choices[0].delta;
          if (delta && delta.content) {
            fullContent += delta.content;
          }
        }
      }
      console.log(`完整内容为：${fullContent}`);
    } else {
      console.log(`非流式输出内容为：${completion.choices[0].message.content}`);
    }
  } catch (err) {
    console.error(`错误信息：${err}`);
  }
}

main();
```

## cURL

```
# ======= 重要提示 =======
# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions
# 新加坡地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
# === 执行时请删除该注释 ===

curl -X POST 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions' \
-H "Authorization: Bearer $DASHSCOPE_API_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "qwen3-asr-flash",
    "messages": [
        {
            "content": [
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"
                    }
                }
            ],
            "role": "user"
        }
    ],
    "stream":false,
    "asr_options": {
        "enable_itn": false
    }
}'
```

## 输入内容：Base64编码的音频文件

可输入Base64编码数据（[Data URL](https://www.rfc-editor.org/rfc/rfc2397)），格式为：`data:<mediatype>;base64,<data>`。

-   `<mediatype>`：MIME类型
    
    因音频格式而异，例如：
    
    -   WAV：`audio/wav`
        
    -   MP3：`audio/mpeg`
        
-   `<data>`：音频转成的Base64编码的字符串
    
    Base64编码会增大体积，请控制原文件大小，确保编码后仍符合输入音频大小限制（10MB）
    
-   示例：`data:audio/wav;base64,SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4LjI5LjEwMAAAAAAAAAAAAAAA//PAxABQ/BXRbMPe4IQAhl9`
    
    **点击查看示例代码**
    
    Python
    
    ```
    import base64, pathlib
    
    # input.mp3为用于声音复刻的本地音频文件，请替换为自己的音频文件路径，确保其符合音频要求
    file_path = pathlib.Path("input.mp3")
    base64_str = base64.b64encode(file_path.read_bytes()).decode()
    data_uri = f"data:audio/mpeg;base64,{base64_str}"
    ```
    
    Java
    
    ```
    import java.nio.file.*;
    import java.util.Base64;
    
    public class Main {
        /**
         * filePath为用于声音复刻的本地音频文件，请替换为自己的音频文件路径，确保其符合音频要求
         */
        public static String toDataUrl(String filePath) throws Exception {
            byte[] bytes = Files.readAllBytes(Paths.get(filePath));
            String encoded = Base64.getEncoder().encodeToString(bytes);
            return "data:audio/mpeg;base64," + encoded;
        }
    
        // 使用示例
        public static void main(String[] args) throws Exception {
            System.out.println(toDataUrl("input.mp3"));
        }
    }
    ```
    

## Python SDK

示例中用到的音频文件为：[welcome.mp3](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260105/wotsae/welcome.mp3)。

```
import base64
from openai import OpenAI
import os
import pathlib

try:
    # 请替换为实际的音频文件路径
    file_path = "welcome.mp3"
    # 请替换为实际的音频文件MIME类型
    audio_mime_type = "audio/mpeg"

    file_path_obj = pathlib.Path(file_path)
    if not file_path_obj.exists():
        raise FileNotFoundError(f"音频文件不存在: {file_path}")

    base64_str = base64.b64encode(file_path_obj.read_bytes()).decode()
    data_uri = f"data:{audio_mime_type};base64,{base64_str}"

    client = OpenAI(
        # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    

    stream_enabled = False  # 是否开启流式输出
    completion = client.chat.completions.create(
        model="qwen3-asr-flash",
        messages=[
            {
                "content": [
                    {
                        "type": "input_audio",
                        "input_audio": {
                            "data": data_uri
                        }
                    }
                ],
                "role": "user"
            }
        ],
        stream=stream_enabled,
        # stream设为False时，不能设置stream_options参数
        # stream_options={"include_usage": True},
        extra_body={
            "asr_options": {
                # "language": "zh",
                "enable_itn": False
            }
        }
    )
    if stream_enabled:
        full_content = ""
        print("流式输出内容为：")
        for chunk in completion:
            # 如果stream_options.include_usage为True，则最后一个chunk的choices字段为空列表，需要跳过（可以通过chunk.usage获取 Token 使用量）
            print(chunk)
            if chunk.choices and chunk.choices[0].delta.content:
                full_content += chunk.choices[0].delta.content
        print(f"完整内容为：{full_content}")
    else:
        print(f"非流式输出内容为：{completion.choices[0].message.content}")
except Exception as e:
    print(f"错误信息：{e}")
```

## Node.js SDK

示例中用到的音频文件为：[welcome.mp3](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260105/wotsae/welcome.mp3)。

```
// 运行前的准备工作:
// Windows/Mac/Linux 通用:
// 1. 确保已安装 Node.js (建议版本 >= 14)
// 2. 运行以下命令安装必要的依赖: npm install openai

import OpenAI from "openai";
import { readFileSync } from 'fs';

const client = new OpenAI({
  // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
  // 若没有配置环境变量，请用百炼API Key将下行替换为：apiKey: "sk-xxx",
  apiKey: process.env.DASHSCOPE_API_KEY,
  // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
  baseURL: "https://dashscope.aliyuncs.com/compatible-mode/v1", 
});

const encodeAudioFile = (audioFilePath) => {
    const audioFile = readFileSync(audioFilePath);
    return audioFile.toString('base64');
};

// 请替换为实际的音频文件路径
const dataUri = `data:audio/mpeg;base64,${encodeAudioFile("welcome.mp3")}`;

async function main() {
  try {
    const streamEnabled = false; // 是否开启流式输出
    const completion = await client.chat.completions.create({
      model: "qwen3-asr-flash",
      messages: [
        {
          role: "user",
          content: [
            {
              type: "input_audio",
              input_audio: {
                data: dataUri
              }
            }
          ]
        }
      ],
      stream: streamEnabled,
      // stream设为False时，不能设置stream_options参数
      // stream_options: {
      //   "include_usage": true
      // },
      extra_body: {
        asr_options: {
          // language: "zh",
          enable_itn: false
        }
      }
    });

    if (streamEnabled) {
      let fullContent = "";
      console.log("流式输出内容为：");
      for await (const chunk of completion) {
        console.log(JSON.stringify(chunk));
        if (chunk.choices && chunk.choices.length > 0) {
          const delta = chunk.choices[0].delta;
          if (delta && delta.content) {
            fullContent += delta.content;
          }
        }
      }
      console.log(`完整内容为：${fullContent}`);
    } else {
      console.log(`非流式输出内容为：${completion.choices[0].message.content}`);
    }
  } catch (err) {
    console.error(`错误信息：${err}`);
  }
}

main();
```

## **API参考**

[录音文件识别-千问API参考](https://help.aliyun.com/zh/model-studio/qwen-asr-api-reference)

## **模型应用上架及备案**

参见[应用合规备案](https://help.aliyun.com/zh/model-studio/compliance-and-launch-filing-guide-for-ai-apps-powered-by-the-tongyi-model)。

## **模型功能特性对比**

下表中qwen3-asr-flash和qwen3-asr-flash-2025-09-08模型的功能特性同样适用于美国（弗吉尼亚）地域对应的qwen3-asr-flash-us和qwen3-asr-flash-2025-09-08-us模型。

| **功能/特性** | **qwen3-asr-flash-filetrans、qwen3-asr-flash-filetrans-2025-11-17** | **qwen3-asr-flash、qwen3-asr-flash-2026-02-10、qwen3-asr-flash-2025-09-08** |
| --- | --- | --- |
| **支持语言** | 中文（普通话、四川话、闽南语、吴语、粤语）、英语、日语、德语、韩语、俄语、法语、葡萄牙语、阿拉伯语、意大利语、西班牙语、印地语、印尼语、泰语、土耳其语、乌克兰语、越南语、捷克语、丹麦语、菲律宾语、芬兰语、冰岛语、马来语、挪威语、波兰语、瑞典语 |   |
| **支持的音频格式** | aac、amr、avi、flac、flv、m4a、mkv、mov、mp3、mp4、mpeg、ogg、opus、wav、webm、wma、wmv | aac、amr、avi、aiff、flac、flv、mkv、mp3、mpeg、ogg、opus、wav、webm、wma、wmv |
| **采样率** | 因音频格式而异： - pcm格式音频：16kHz - 其他格式音频：任意（服务端会先将音频重采样为 16 kHz，再进行识别） |   |
| **声道** | 任意 不同模型在处理多声道音频时方式存在差异： - 千问3-ASR-Flash-Filetrans：需通过`channel_id`参数指定音轨索引 - 千问3-ASR-Flash：无需额外处理，模型会对多声道音频做均值合并后再处理 |   |
| **输入形式** | 公网可访问的待识别文件URL | Base64编码的文件、本地文件绝对路径、公网可访问的待识别文件URL |
| **音频大小/时长** | 音频文件大小不超过2GB，且时长不超过12小时 | 音频文件大小不超过10MB，且时长不超过5分钟 |
| **情感识别** | 支持 固定开启，可通过响应参数`emotion`查看结果 |   |
| **时间戳** | 支持 固定开启，可通过请求参数`enable_words`控制时间戳级别 > 字级别时间戳仅支持以下语种：中文、英语、日语、韩语、德语、法语、西班牙语、意大利语、葡萄牙语、俄语，其他语种可能无法保证准确性 | 不支持 |
| **标点符号预测** | 支持 固定开启 |   |
| **热词** | 不支持 |   |
| **ITN** | 支持 默认关闭，可开启，仅适用于中、英文 |   |
| **歌唱识别** | 支持 固定开启 |   |
| **噪声拒识** | 支持 固定开启 |   |
| **敏感词过滤** | 不支持 |   |
| **说话人分离** | 不支持 |   |
| **语气词过滤** | 不支持 |   |
| **VAD** | 支持 固定开启 | 不支持 |
| **限流（RPM）** | 100 |   |
| **接入方式** | DashScope：Java/Python SDK、RESTful API | DashScope：Java/Python SDK、RESTful API OpenAI：Python/Node.js SDK、RESTful API |
| **价格** | 中国内地：0.00022元/秒 美国：0.000035元/秒 国际：0.00026元/秒 |   |

## 常见问题

### **Q：如何为API提供公网可访问的音频URL？**

推荐使用[阿里云对象存储OSS](https://help.aliyun.com/zh/oss/user-guide/simple-upload#a632b50f190j8)，它提供了高可用、高可靠的存储服务，并且可以方便地生成公网访问URL。

**在公网环境下验证生成的 URL 可正常访问：**可在浏览器或通过 curl 命令访问该 URL，确保音频文件能够成功下载或播放（HTTP状态码为200）。

### **Q：如何检查音频格式是否符合要求？**

可以使用开源工具[ffprobe](https://ffmpeg.org/ffprobe.html)快速获取音频的详细信息：

```
# 查询音频的容器格式(format_name)、编码(codec_name)、采样率(sample_rate)、声道数(channels)
ffprobe -v error -show_entries format=format_name -show_entries stream=codec_name,sample_rate,channels -of default=noprint_wrappers=1 your_audio_file.mp3
```

### **Q：**如何处理音频以满足模型要求？

可以使用开源工具[FFmpeg](https://ffmpeg.en.lo4d.com/download)对音频进行裁剪或格式转换：

-   **音频裁剪：从长音频中截取片段**
    
    ```
    # -i: 输入文件
    # -ss 00:01:30: 设置裁剪的起始时间 (从1分30秒开始)
    # -t 00:02:00: 设置裁剪的持续时长 (裁剪2分钟)
    # -c copy: 直接复制音频流，不重新编码，速度快
    # output_clip.wav: 输出文件
    ffmpeg -i long_audio.wav -ss 00:01:30 -t 00:02:00 -c copy output_clip.wav
    ```
    
-   **格式转换**
    
    例如，将任意音频转换为16kHz、16-bit、单声道WAV文件
    
    ```
    # -i: 输入文件
    # -ac 1: 设置声道数为1 (单声道)
    # -ar 16000: 设置采样率为16000Hz (16kHz)
    # -sample_fmt s16: 设置采样格式为16-bit signed integer PCM
    # output.wav: 输出文件
    ffmpeg -i input.mp3 -ac 1 -ar 16000 -sample_fmt s16 output.wav
    ```
    

/\* 让引用上下间距调小，避免内容显示过于稀疏 \*/ .unionContainer .markdown-body blockquote { margin: 4px 0; } .aliyun-docs-content table.qwen blockquote { border-left: none; /\* 添加这一行来移除表格里的引用文字的左侧边框 \*/ padding-left: 5px; /\* 左侧内边距 \*/ margin: 4px 0; }

 span.aliyun-docs-icon { color: transparent !important; font-size: 0 !important; } span.aliyun-docs-icon:before { color: black; font-size: 16px; } span.aliyun-docs-icon.icon-size-20:before { font-size: 20px; } span.aliyun-docs-icon.icon-size-22:before { font-size: 22px; } span.aliyun-docs-icon.icon-size-24:before { font-size: 24px; } span.aliyun-docs-icon.icon-size-26:before { font-size: 26px; } span.aliyun-docs-icon.icon-size-28:before { font-size: 28px; }

# 录音文件识别（Qwen-ASR）API参考

本文介绍 Qwen-ASR 模型的输入与输出参数。可通过OpenAI 兼容或DashScope协议调用 API。

**用户指南：**模型介绍和选型请参见[录音文件识别-千问](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition)。

## **模型接入方式**

不同[模型](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#b8c8c0483153o)支持的接入方式不同，请根据下表选择正确的方式进行集成。

| **模型** | **接入方式** |
| --- | --- |
| 千问3-ASR-Flash-Filetrans | 仅支持[DashScope异步调用](#9937e8884002q)方式 |
| 千问3-ASR-Flash | [OpenAI 兼容](#d397bcc41eu3q)和[DashScope同步调用](#1afc6b20a29ie)两种方式 |

## **OpenAI 兼容**

### **URL**

## 中国内地

服务部署范围为[中国内地](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**北京接入地域**，模型推理计算资源仅限于中国内地。

HTTP请求地址：`POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions`

SDK调用配置的base\_url：`https://dashscope.aliyuncs.com/compatible-mode/v1`

## 国际

服务部署范围为[国际](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**新加坡接入地域**，模型推理计算资源在全球范围内动态调度（不含中国内地）。

HTTP请求地址：`POST https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions`

SDK调用配置的base\_url：`https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

| ### **请求体** | ### 输入内容：音频文件URL #### Python SDK ``` from openai import OpenAI import os try: client = OpenAI( # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx", api_key=os.getenv("DASHSCOPE_API_KEY"), # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1 base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", ) stream_enabled = False # 是否开启流式输出 completion = client.chat.completions.create( model="qwen3-asr-flash", messages=[ { "content": [ { "type": "input_audio", "input_audio": { "data": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" } } ], "role": "user" } ], stream=stream_enabled, # stream设为False时，不能设置stream_options参数 # stream_options={"include_usage": True}, extra_body={ "asr_options": { # "language": "zh", "enable_itn": False } } ) if stream_enabled: full_content = "" print("流式输出内容为：") for chunk in completion: # 如果stream_options.include_usage为True，则最后一个chunk的choices字段为空列表，需要跳过（可以通过chunk.usage获取 Token 使用量） print(chunk) if chunk.choices and chunk.choices[0].delta.content: full_content += chunk.choices[0].delta.content print(f"完整内容为：{full_content}") else: print(f"非流式输出内容为：{completion.choices[0].message.content}") except Exception as e: print(f"错误信息：{e}") ``` #### Node.js SDK ``` // 运行前的准备工作: // Windows/Mac/Linux 通用: // 1. 确保已安装 Node.js (建议版本 >= 14) // 2. 运行以下命令安装必要的依赖: npm install openai import OpenAI from "openai"; const client = new OpenAI({ // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key // 若没有配置环境变量，请用百炼API Key将下行替换为：apiKey: "sk-xxx", apiKey: process.env.DASHSCOPE_API_KEY, // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1 baseURL: "https://dashscope.aliyuncs.com/compatible-mode/v1", }); async function main() { try { const streamEnabled = false; // 是否开启流式输出 const completion = await client.chat.completions.create({ model: "qwen3-asr-flash", messages: [ { role: "user", content: [ { type: "input_audio", input_audio: { data: "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" } } ] } ], stream: streamEnabled, // stream设为False时，不能设置stream_options参数 // stream_options: { // "include_usage": true // }, extra_body: { asr_options: { // language: "zh", enable_itn: false } } }); if (streamEnabled) { let fullContent = ""; console.log("流式输出内容为："); for await (const chunk of completion) { console.log(JSON.stringify(chunk)); if (chunk.choices && chunk.choices.length > 0) { const delta = chunk.choices[0].delta; if (delta && delta.content) { fullContent += delta.content; } } } console.log(`完整内容为：${fullContent}`); } else { console.log(`非流式输出内容为：${completion.choices[0].message.content}`); } } catch (err) { console.error(`错误信息：${err}`); } } main(); ``` #### cURL ``` # ======= 重要提示 ======= # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions # 新加坡地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # === 执行时请删除该注释 === curl -X POST 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions' \\ -H "Authorization: Bearer $DASHSCOPE_API_KEY" \\ -H "Content-Type: application/json" \\ -d '{ "model": "qwen3-asr-flash", "messages": [ { "content": [ { "type": "input_audio", "input_audio": { "data": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" } } ], "role": "user" } ], "stream":false, "asr_options": { "enable_itn": false } }' ``` ### 输入内容：Base64编码的音频文件 可输入Base64编码数据（[Data URL](https://www.rfc-editor.org/rfc/rfc2397)），格式为：`data:<mediatype>;base64,<data>`。 - `<mediatype>`：MIME类型 因音频格式而异，例如： - WAV：`audio/wav` - MP3：`audio/mpeg` - `<data>`：音频转成的Base64编码的字符串 Base64编码会增大体积，请控制原文件大小，确保编码后仍符合输入音频大小限制（10MB） - 示例：`data:audio/wav;base64,SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4LjI5LjEwMAAAAAAAAAAAAAAA//PAxABQ/BXRbMPe4IQAhl9` **点击查看示例代码** Python ``` import base64, pathlib # input.mp3为用于声音复刻的本地音频文件，请替换为自己的音频文件路径，确保其符合音频要求 file_path = pathlib.Path("input.mp3") base64_str = base64.b64encode(file_path.read_bytes()).decode() data_uri = f"data:audio/mpeg;base64,{base64_str}" ``` Java ``` import java.nio.file.*; import java.util.Base64; public class Main { /** * filePath为用于声音复刻的本地音频文件，请替换为自己的音频文件路径，确保其符合音频要求 */ public static String toDataUrl(String filePath) throws Exception { byte[] bytes = Files.readAllBytes(Paths.get(filePath)); String encoded = Base64.getEncoder().encodeToString(bytes); return "data:audio/mpeg;base64," + encoded; } // 使用示例 public static void main(String[] args) throws Exception { System.out.println(toDataUrl("input.mp3")); } } ``` #### Python SDK 示例中用到的音频文件为：[welcome.mp3](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260105/wotsae/welcome.mp3)。 ``` import base64 from openai import OpenAI import os import pathlib try: # 请替换为实际的音频文件路径 file_path = "welcome.mp3" # 请替换为实际的音频文件MIME类型 audio_mime_type = "audio/mpeg" file_path_obj = pathlib.Path(file_path) if not file_path_obj.exists(): raise FileNotFoundError(f"音频文件不存在: {file_path}") base64_str = base64.b64encode(file_path_obj.read_bytes()).decode() data_uri = f"data:{audio_mime_type};base64,{base64_str}" client = OpenAI( # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx", api_key=os.getenv("DASHSCOPE_API_KEY"), # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1 base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", ) stream_enabled = False # 是否开启流式输出 completion = client.chat.completions.create( model="qwen3-asr-flash", messages=[ { "content": [ { "type": "input_audio", "input_audio": { "data": data_uri } } ], "role": "user" } ], stream=stream_enabled, # stream设为False时，不能设置stream_options参数 # stream_options={"include_usage": True}, extra_body={ "asr_options": { # "language": "zh", "enable_itn": False } } ) if stream_enabled: full_content = "" print("流式输出内容为：") for chunk in completion: # 如果stream_options.include_usage为True，则最后一个chunk的choices字段为空列表，需要跳过（可以通过chunk.usage获取 Token 使用量） print(chunk) if chunk.choices and chunk.choices[0].delta.content: full_content += chunk.choices[0].delta.content print(f"完整内容为：{full_content}") else: print(f"非流式输出内容为：{completion.choices[0].message.content}") except Exception as e: print(f"错误信息：{e}") ``` #### Node.js SDK 示例中用到的音频文件为：[welcome.mp3](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260105/wotsae/welcome.mp3)。 ``` // 运行前的准备工作: // Windows/Mac/Linux 通用: // 1. 确保已安装 Node.js (建议版本 >= 14) // 2. 运行以下命令安装必要的依赖: npm install openai import OpenAI from "openai"; import { readFileSync } from 'fs'; const client = new OpenAI({ // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key // 若没有配置环境变量，请用百炼API Key将下行替换为：apiKey: "sk-xxx", apiKey: process.env.DASHSCOPE_API_KEY, // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1 baseURL: "https://dashscope.aliyuncs.com/compatible-mode/v1", }); const encodeAudioFile = (audioFilePath) => { const audioFile = readFileSync(audioFilePath); return audioFile.toString('base64'); }; // 请替换为实际的音频文件路径 const dataUri = `data:audio/mpeg;base64,${encodeAudioFile("welcome.mp3")}`; async function main() { try { const streamEnabled = false; // 是否开启流式输出 const completion = await client.chat.completions.create({ model: "qwen3-asr-flash", messages: [ { role: "user", content: [ { type: "input_audio", input_audio: { data: dataUri } } ] } ], stream: streamEnabled, // stream设为False时，不能设置stream_options参数 // stream_options: { // "include_usage": true // }, extra_body: { asr_options: { // language: "zh", enable_itn: false } } }); if (streamEnabled) { let fullContent = ""; console.log("流式输出内容为："); for await (const chunk of completion) { console.log(JSON.stringify(chunk)); if (chunk.choices && chunk.choices.length > 0) { const delta = chunk.choices[0].delta; if (delta && delta.content) { fullContent += delta.content; } } } console.log(`完整内容为：${fullContent}`); } else { console.log(`非流式输出内容为：${completion.choices[0].message.content}`); } } catch (err) { console.error(`错误信息：${err}`); } } main(); ``` |
| --- | --- |
| **model** `*string*` **（必选）** [模型](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#b8c8c0483153o)名称。仅适用于千问3-ASR-Flash模型。 |
| **messages** `*array*` **（必选）** 消息列表。 **消息类型** System Message `*object*`（可选） 模型的目标或角色。如果设置系统消息，请放在messages列表的第一位。 **属性** **role** `*string*` **（必选）** 固定为`system`。 User Message `*object*`**（必选）** 用户发送给模型的消息。 **属性** **content** `*array*` **（必选）** 用户消息的内容。仅允许设置一组消息。 **属性** **type** `*string*`**（必选）** 固定为`input_audio`，代表输入的是音频。 **input\\_audio** `*string*`**（必选）** 待识别音频。具体用法请参见[快速开始](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#7818a3bc466d6)。 千问3-ASR-Flash模型在OpenAI兼容模式下支持两种输入形式：Base64编码的文件和公网可访问的待识别文件URL。 使用SDK时，若录音文件存储在[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/simple-upload#a632b50f190j8)，不支持使用以 `oss://`为前缀的临时 URL。 使用RESTful API时，若录音文件存储在[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/simple-upload#a632b50f190j8)，支持使用以 `oss://`为前缀的临时 URL。但需注意： **重要** - 临时 URL 有效期48小时，过期后无法使用，**请勿用于生产环境。** - 文件上传凭证接口限流为 100 QPS 且不支持扩容，**请勿用于生产环境、高并发及压测场景。** - 生产环境建议使用[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/what-is-oss) 等稳定存储，确保文件长期可用并规避限流问题。 **role** `*string*` **（必选）** 用户消息的角色，固定为`user`。 |
| **asr\\_options** `*object*` （可选） 用来指定某些功能是否启用。 > `asr_options`非OpenAI标准参数，若使用OpenAI SDK，请通过`extra_body`传入。 **属性** **language** *string*（可选）无默认值 若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率。 只能指定一个语种。 若音频语种不确定，或包含多种语种（例如中英日韩混合），请勿指定该参数。 **取值范围** - zh：中文（普通话、四川话、闽南语、吴语） - yue：粤语 - en：英文 - ja：日语 - de：德语 - ko：韩语 - ru：俄语 - fr：法语 - pt：葡萄牙语 - ar：阿拉伯语 - it：意大利语 - es：西班牙语 - hi：印地语 - id：印尼语 - th：泰语 - tr：土耳其语 - uk：乌克兰语 - vi：越南语 - cs：捷克语 - da：丹麦语 - fil：菲律宾语 - fi：芬兰语 - is：冰岛语 - ms：马来语 - no：挪威语 - pl：波兰语 - sv：瑞典语 **enable\\_itn** `*boolean*`（可选）默认值为`false` 是否启用ITN（Inverse Text Normalization，逆文本标准化）。该功能仅适用于中文和英文音频。 参数值： - true：开启； - false：关闭。 |
| **stream** `*boolean*` （可选）默认值为`false` 是否以流式输出方式回复。相关文档：[流式输出](https://help.aliyun.com/zh/model-studio/stream) 可选值： - `false`：模型生成全部内容后一次性返回； - `true`：边生成边输出，每生成一部分内容即返回一个数据块（chunk）。需实时逐个读取这些块以拼接完整回复。 推荐设置为`true`，可提升阅读体验并降低超时风险。 |
| **stream\\_options** `*object*` （可选） 流式输出的配置项，仅在 `stream` 为 `true` 时生效。 **属性** **include\\_usage** `*boolean*` （可选）默认值为`false` 是否在响应的最后一个数据块包含Token消耗信息。 可选值： - `true`：包含； - `false`：不包含。 > 流式输出时，Token 消耗信息仅可出现在响应的最后一个数据块。 |

| ### **返回体** | ## 非流式输出 ``` { "choices": [ { "finish_reason": "stop", "index": 0, "message": { "annotations": [ { "emotion": "neutral", "language": "zh", "type": "audio_info" } ], "content": "欢迎使用阿里云。", "role": "assistant" } } ], "created": 1767683986, "id": "chatcmpl-487abe5f-d4f2-9363-a877-xxxxxxx", "model": "qwen3-asr-flash", "object": "chat.completion", "usage": { "completion_tokens": 12, "completion_tokens_details": { "text_tokens": 12 }, "prompt_tokens": 42, "prompt_tokens_details": { "audio_tokens": 42, "text_tokens": 0 }, "seconds": 1, "total_tokens": 54 } } ``` ## 流式输出 ``` data: {"model":"qwen3-asr-flash","id":"chatcmpl-3fb97803-d27f-9289-8889-xxxxx","created":1767685989,"object":"chat.completion.chunk","usage":null,"choices":[{"logprobs":null,"index":0,"delta":{"content":"","role":"assistant"}}]} data: {"model":"qwen3-asr-flash","id":"chatcmpl-3fb97803-d27f-9289-8889-xxxxx","choices":[{"delta":{"annotations":[{"type":"audio_info","language":"zh","emotion":"neutral"}],"content":"欢迎","role":null},"index":0}],"created":1767685989,"object":"chat.completion.chunk","usage":null} data: {"model":"qwen3-asr-flash","id":"chatcmpl-3fb97803-d27f-9289-8889-xxxxx","choices":[{"delta":{"annotations":[{"type":"audio_info","language":"zh","emotion":"neutral"}],"content":"使用","role":null},"index":0}],"created":1767685989,"object":"chat.completion.chunk","usage":null} data: {"model":"qwen3-asr-flash","id":"chatcmpl-3fb97803-d27f-9289-8889-xxxxx","choices":[{"delta":{"annotations":[{"type":"audio_info","language":"zh","emotion":"neutral"}],"content":"阿里","role":null},"index":0}],"created":1767685989,"object":"chat.completion.chunk","usage":null} data: {"model":"qwen3-asr-flash","id":"chatcmpl-3fb97803-d27f-9289-8889-xxxxx","choices":[{"delta":{"annotations":[{"type":"audio_info","language":"zh","emotion":"neutral"}],"content":"云","role":null},"index":0}],"created":1767685989,"object":"chat.completion.chunk","usage":null} data: {"model":"qwen3-asr-flash","id":"chatcmpl-3fb97803-d27f-9289-8889-xxxxx","choices":[{"delta":{"annotations":[{"type":"audio_info","language":"zh","emotion":"neutral"}],"content":"。","role":null},"index":0}],"created":1767685989,"object":"chat.completion.chunk","usage":null} data: {"model":"qwen3-asr-flash","id":"chatcmpl-3fb97803-d27f-9289-8889-xxxxx","choices":[{"delta":{"role":null},"index":0,"finish_reason":"stop"}],"created":1767685989,"object":"chat.completion.chunk","usage":null} data: [DONE] ``` |
| --- | --- |
| **id** `*string*` 本次调用的唯一标识符。 |
| **choices** `*array*` 模型的输出信息。 **属性** **finish\\_reason** `*string*` 有三种情况： - 正在生成时为null； - 因模型输出自然结束，或触发输入参数中的stop条件而结束时为stop； - 因生成长度过长而结束为length。 **index** `*integer*` 当前对象在`choices`数组中的索引。 **message** `*object*` 模型输出的消息对象。 **属性** **role** `*string*` 输出消息的角色，固定为assistant。 **content** `*array*` 语音识别结果。 **annotations** `*array*` 输出标注信息（如语种） **属性** **language** `*string*` 被识别音频的语种。当请求参数`language`已指定语种时，该值与所指定的参数一致。 **取值范围** - zh：中文（普通话、四川话、闽南语、吴语） - yue：粤语 - en：英文 - ja：日语 - de：德语 - ko：韩语 - ru：俄语 - fr：法语 - pt：葡萄牙语 - ar：阿拉伯语 - it：意大利语 - es：西班牙语 - hi：印地语 - id：印尼语 - th：泰语 - tr：土耳其语 - uk：乌克兰语 - vi：越南语 - cs：捷克语 - da：丹麦语 - fil：菲律宾语 - fi：芬兰语 - is：冰岛语 - ms：马来语 - no：挪威语 - pl：波兰语 - sv：瑞典语 **type** `*string*` 固定为`audio_info`，表示音频信息。 **emotion** `*string*` 被识别音频的情感。支持的情感如下： - `surprised`：惊讶 - `neutral`：平静 - `happy`：愉快 - `sad`：悲伤 - `disgusted`：厌恶 - `angry`：愤怒 - `fearful`：恐惧 |
| **created** `*integer*` 请求创建时的 Unix 时间戳（秒）。 |
| **model** `*string*` 本次请求使用的模型。 |
| **object** `*string*` 始终为`chat.completion`。 |
| **usage** `*object*` 本次请求的Token消耗信息。 **属性** **completion\\_tokens** `*integer*` 模型输出的 Token 数。 **completion\\_tokens\\_details** `*object*` 模型输出的 Token 细粒度详情。 **属性** **text\\_tokens** `*integer*` 模型输出文本的Token数。 **prompt\\_tokens** `*object*` 输入的Token数。 **prompt\\_tokens\\_details** `*object*` 输入的 Token 细粒度详情。 **属性** **audio\\_tokens** `*integer*` 输入音频长度（Token）。音频转换Token规则：每秒音频转换为25个Token，不足1秒按1秒计算。 **text\\_tokens** `*integer*` 无需关注该参数。 **seconds** `*integer*` 音频时长（秒）。 **total\\_tokens** `*integer*` 输入和输出总Token数（`total_tokens = completion_tokens + prompt_tokens`）。 |

## **DashScope同步调用**

### **URL**

## 中国内地

服务部署范围为[中国内地](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**北京接入地域**，模型推理计算资源仅限于中国内地。

HTTP请求地址：`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

SDK调用配置的base\_url：`https://dashscope.aliyuncs.com/api/v1`

## 国际

服务部署范围为[国际](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**新加坡接入地域**，模型推理计算资源在全球范围内动态调度（不含中国内地）。

HTTP请求地址：`POST https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

SDK调用配置的base\_url：`https://dashscope-intl.aliyuncs.com/api/v1`

## 美国

服务部署范围为[美国](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**美国（弗吉尼亚）接入地域**，模型推理计算资源仅限于美国境内。

HTTP请求地址：`POST https://dashscope-us.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

SDK调用配置的base\_url：`https://dashscope-us.aliyuncs.com/api/v1`

| ### **请求体** | 以下示例为音频 URL 识别；本地音频文件识别示例请参见[快速开始](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#7818a3bc466d6)。 ## cURL ``` # ======= 重要提示 ======= # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation # 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若使用美国地域的模型，需要加us后缀 # === 执行时请删除该注释 === curl -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation" \\ -H "Authorization: Bearer $DASHSCOPE_API_KEY" \\ -H "Content-Type: application/json" \\ -d '{ "model": "qwen3-asr-flash", "input": { "messages": [ { "content": [ { "text": "" } ], "role": "system" }, { "content": [ { "audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" } ], "role": "user" } ] }, "parameters": { "asr_options": { "enable_itn": false } } }' ``` ## Java ``` import java.util.Arrays; import java.util.Collections; import java.util.HashMap; import java.util.Map; import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversation; import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationParam; import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationResult; import com.alibaba.dashscope.common.MultiModalMessage; import com.alibaba.dashscope.common.Role; import com.alibaba.dashscope.exception.ApiException; import com.alibaba.dashscope.exception.NoApiKeyException; import com.alibaba.dashscope.exception.UploadFileException; import com.alibaba.dashscope.utils.Constants; import com.alibaba.dashscope.utils.JsonUtils; public class Main { public static void simpleMultiModalConversationCall() throws ApiException, NoApiKeyException, UploadFileException { MultiModalConversation conv = new MultiModalConversation(); MultiModalMessage userMessage = MultiModalMessage.builder() .role(Role.USER.getValue()) .content(Arrays.asList( Collections.singletonMap("audio", "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"))) .build(); Map<String, Object> asrOptions = new HashMap<>(); asrOptions.put("enable_itn", false); // asrOptions.put("language", "zh"); // 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率 MultiModalConversationParam param = MultiModalConversationParam.builder() // 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key // 若没有配置环境变量，请用百炼API Key将下行替换为：.apiKey("sk-xxx") .apiKey(System.getenv("DASHSCOPE_API_KEY")) // 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us .model("qwen3-asr-flash") .message(userMessage) .parameter("asr_options", asrOptions) .build(); MultiModalConversationResult result = conv.call(param); System.out.println(JsonUtils.toJson(result)); } public static void main(String[] args) { try { // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1 Constants.baseHttpApiUrl = "https://dashscope.aliyuncs.com/api/v1"; simpleMultiModalConversationCall(); } catch (ApiException \\| NoApiKeyException \\| UploadFileException e) { System.out.println(e.getMessage()); } System.exit(0); } } ``` ## Python ``` import os import dashscope # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1，若使用美国地域的模型，需将url替换为：https://dashscope-us.aliyuncs.com/api/v1 dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1' messages = [ {"role": "user", "content": [{"audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"}]} ] response = dashscope.MultiModalConversation.call( # 新加坡/美国地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx" api_key=os.getenv("DASHSCOPE_API_KEY"), # 若使用美国地域的模型，需在模型后面加上“-us”后缀，例如qwen3-asr-flash-us model="qwen3-asr-flash", messages=messages, result_format="message", asr_options={ # "language": "zh", # 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率 "enable_itn":False } ) print(response) ``` |
| --- | --- | --- | --- |
| **model** `*string*` **（必选）** [模型](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#b8c8c0483153o)名称。仅适用于千问3-ASR-Flash模型。 |
| **messages** `*array*` **（必选）** 消息列表。 > 通过HTTP调用时，请将**messages** 放入 **input** 对象中。 **消息类型** System Message `*object*`（可选） 模型的目标或角色。如果设置系统消息，请放在messages列表的第一位。 仅千问3-ASR-Flash支持该参数。 **属性** **role** `*string*` **（必选）** 固定为`system`。 User Message `*object*`**（必选）** 用户发送给模型的消息。 **属性** **content** `*array*` **（必选）** 用户消息的内容。仅允许设置一组消息。 **属性** **audio** `*string*`**（必选）** 待识别音频。具体用法请参见[快速开始](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#7818a3bc466d6)。 千问3-ASR-Flash模型在DashScope调用方式下支持三种输入形式：Base64编码的文件、本地文件绝对路径、公网可访问的待识别文件URL。 使用SDK时，若录音文件存储在[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/simple-upload#a632b50f190j8)，不支持使用以 `oss://`为前缀的临时 URL。 使用RESTful API时，若录音文件存储在[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/simple-upload#a632b50f190j8)，支持使用以 `oss://`为前缀的临时 URL。但需注意： **重要** - 临时 URL 有效期48小时，过期后无法使用，**请勿用于生产环境。** - 文件上传凭证接口限流为 100 QPS 且不支持扩容，**请勿用于生产环境、高并发及压测场景。** - 生产环境建议使用[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/what-is-oss) 等稳定存储，确保文件长期可用并规避限流问题。 **role** `*string*` **（必选）** 用户消息的角色，固定为`user`。 |
| **asr\\_options** `*object*` （可选） 用来指定某些功能是否启用。 仅千问3-ASR-Flash支持该参数。 **属性** **language** *string*（可选）无默认值 若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率。 只能指定一个语种。 若音频语种不确定，或包含多种语种（例如中英日韩混合），请勿指定该参数。 **取值范围** - zh：中文（普通话、四川话、闽南语、吴语） - yue：粤语 - en：英文 - ja：日语 - de：德语 - ko：韩语 - ru：俄语 - fr：法语 - pt：葡萄牙语 - ar：阿拉伯语 - it：意大利语 - es：西班牙语 - hi：印地语 - id：印尼语 - th：泰语 - tr：土耳其语 - uk：乌克兰语 - vi：越南语 - cs：捷克语 - da：丹麦语 - fil：菲律宾语 - fi：芬兰语 - is：冰岛语 - ms：马来语 - no：挪威语 - pl：波兰语 - sv：瑞典语 **enable\\_itn** `*boolean*`（可选）默认值为`false` 是否启用ITN（Inverse Text Normalization，逆文本标准化）。该功能仅适用于中文和英文音频。 参数值： - true：开启； - false：关闭。 |

| ### **返回体** | ``` { "output": { "choices": [ { "finish_reason": "stop", "message": { "annotations": [ { "language": "zh", "type": "audio_info", "emotion": "neutral" } ], "content": [ { "text": "欢迎使用阿里云。" } ], "role": "assistant" } } ] }, "usage": { "input_tokens_details": { "text_tokens": 0 }, "output_tokens_details": { "text_tokens": 6 }, "seconds": 1 }, "request_id": "568e2bf0-d6f2-97f8-9f15-a57b11dc6977" } ``` |
| --- | --- |
| **request\\_id** `*string*` 本次调用的唯一标识符。 > Java SDK返回参数为**requestId。** |
| **output** `*object*` 调用结果信息。 **属性** **choices** `*array*` 模型的输出信息。当result\\_format为message时返回choices参数。 **属性** **finish\\_reason** `*string*` 有三种情况： - 正在生成时为null； - 因模型输出自然结束，或触发输入参数中的stop条件而结束时为stop； - 因生成长度过长而结束为length。 **message** `*object*` 模型输出的消息对象。 **属性** **role** `*string*` 输出消息的角色，固定为assistant。 **content** `*array*` 输出消息的内容。 **属性** **text** `*string*` 语音识别结果。 **annotations** `*array*` 输出标注信息（如语种） **属性** **language** `*string*` 被识别音频的语种。当请求参数`language`已指定语种时，该值与所指定的参数一致。 **取值范围** - zh：中文（普通话、四川话、闽南语、吴语） - yue：粤语 - en：英文 - ja：日语 - de：德语 - ko：韩语 - ru：俄语 - fr：法语 - pt：葡萄牙语 - ar：阿拉伯语 - it：意大利语 - es：西班牙语 - hi：印地语 - id：印尼语 - th：泰语 - tr：土耳其语 - uk：乌克兰语 - vi：越南语 - cs：捷克语 - da：丹麦语 - fil：菲律宾语 - fi：芬兰语 - is：冰岛语 - ms：马来语 - no：挪威语 - pl：波兰语 - sv：瑞典语 **type** `*string*` 固定为`audio_info`，表示音频信息。 **emotion** `*string*` 被识别音频的情感。支持的情感如下： - `surprised`：惊讶 - `neutral`：平静 - `happy`：愉快 - `sad`：悲伤 - `disgusted`：厌恶 - `angry`：愤怒 - `fearful`：恐惧 |
| **usage** `*object*` 本次请求的Token消耗信息。 **属性** **input\\_tokens\\_details** `*object*` 千问3-ASR-Flash输入内容长度（Token）。 **属性** **text\\_tokens** `*integer*` 无需关注该参数。 **output\\_tokens\\_details** `*object*` 千问3-ASR-Flash输出内容长度（Token）。 **属性** **text\\_tokens** `*integer*` 千问3-ASR-Flash输出的识别结果文本长度（Token）。 **seconds** `*integer*` 千问3-ASR-Flash音频时长（秒）。 |

## **DashScope异步调用**

### **流程说明**

与OpenAI兼容模式或DashScope同步调用（均为一次请求、立即返回结果）不同，异步调用专为处理长音频文件或耗时较长的任务设计，该模式采用“提交-轮询”的两步式流程，避免了因长时间等待而导致的请求超时：

1.  第一步：提交任务
    
    -   客户端发起一个异步处理请求。
        
    -   服务器验证请求后，不会立即执行任务，而是返回一个唯一的 `task_id`，表示任务已成功创建。
        
2.  第二步：获取结果
    
    -   客户端使用获取到的 `task_id`，通过轮询方式反复调用结果查询接口。
        
    -   当任务处理完成后，结果查询接口将返回最终的识别结果。
        

您可以根据集成环境选择使用SDK或直接调用RESTful API。

-   使用 SDK（示例代码请参见[快速开始](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#7818a3bc466d6)，请求参数请参见[提交任务](#88657039c4x0g)的[请求体](#1a2369eebaueh)，返回结果请参见[异步调用识别结果说明](#2c27ad3e80p4y)）
    
    SDK封装了底层的API调用细节，提供了更便捷的编程体验。
    
    1.  提交任务：调用 `async_call()` (Python) 或 `asyncCall()` (Java) 方法提交任务。此方法将返回一个包含 `task_id` 的任务对象。
        
    2.  获取结果：使用上一步返回的任务对象或 `task_id`，调用 `fetch()` 方法获取结果。SDK内部会自动处理轮询逻辑，直到任务完成或超时。
        
-   2\. 使用 RESTful API
    
    直接调用HTTP接口提供了最大的灵活性。
    
    1.  [提交任务](#88657039c4x0g)，如果请求成功，[返回体](#eca6c7d3f35hn)中将包含一个 `task_id`。
        
    2.  使用上一步获取的 `task_id`，[获取任务执行结果](#f9109f6ea3di2)。
        

### **提交任务**

#### **URL**

## 中国内地

服务部署范围为[中国内地](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**北京接入地域**，模型推理计算资源仅限于中国内地。

HTTP请求地址：`POST https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription`

SDK调用配置的base\_url：`https://dashscope.aliyuncs.com/api/v1`

## 国际

服务部署范围为[国际](https://help.aliyun.com/zh/model-studio/regions/#080da663a75xh)时，数据存储位于**新加坡接入地域**，模型推理计算资源在全球范围内动态调度（不含中国内地）。

HTTP请求地址：`POST https://dashscope-intl.aliyuncs.com/api/v1/services/audio/asr/transcription`

SDK调用配置的base\_url：`https://dashscope-intl.aliyuncs.com/api/v1`

| #### **请求体** | ## cURL ``` # ======= 重要提示 ======= # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/audio/asr/transcription # 新加坡地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # === 执行时请删除该注释 === curl --location --request POST 'https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription' \\ --header "Authorization: Bearer $DASHSCOPE_API_KEY" \\ --header "Content-Type: application/json" \\ --header "X-DashScope-Async: enable" \\ --data '{ "model": "qwen3-asr-flash-filetrans", "input": { "file_url": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" }, "parameters": { "channel_id":[ 0 ], "enable_itn": false } }' ``` ## Java SDK示例请参见[快速开始](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#7818a3bc466d6)。 ``` import com.google.gson.Gson; import com.google.gson.annotations.SerializedName; import okhttp3.*; import java.io.IOException; public class Main { // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/audio/asr/transcription private static final String API_URL = "https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription"; public static void main(String[] args) { // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key // 若没有配置环境变量，请用百炼API Key将下行替换为：String apiKey = "sk-xxx" String apiKey = System.getenv("DASHSCOPE_API_KEY"); OkHttpClient client = new OkHttpClient(); Gson gson = new Gson(); /*String payloadJson = """ { "model": "qwen3-asr-flash-filetrans", "input": { "file_url": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" }, "parameters": { "channel_id": [0], "enable_itn": false, "language": "zh", "corpus": { "text": "" } } } """;*/ String payloadJson = """ { "model": "qwen3-asr-flash-filetrans", "input": { "file_url": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" }, "parameters": { "channel_id": [0], "enable_itn": false } } """; RequestBody body = RequestBody.create(payloadJson, MediaType.get("application/json; charset=utf-8")); Request request = new Request.Builder() .url(API_URL) .addHeader("Authorization", "Bearer " + apiKey) .addHeader("Content-Type", "application/json") .addHeader("X-DashScope-Async", "enable") .post(body) .build(); try (Response response = client.newCall(request).execute()) { if (response.isSuccessful() && response.body() != null) { String respBody = response.body().string(); // 用 Gson 解析 JSON ApiResponse apiResp = gson.fromJson(respBody, ApiResponse.class); if (apiResp.output != null) { System.out.println("task_id: " + apiResp.output.taskId); } else { System.out.println(respBody); } } else { System.out.println("task failed! HTTP code: " + response.code()); if (response.body() != null) { System.out.println(response.body().string()); } } } catch (IOException e) { e.printStackTrace(); } } static class ApiResponse { @SerializedName("request_id") String requestId; Output output; } static class Output { @SerializedName("task_id") String taskId; @SerializedName("task_status") String taskStatus; } } ``` ## Python SDK示例请参见[快速开始](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#7818a3bc466d6)。 ``` import requests import json import os # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/services/audio/asr/transcription url = "https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription" # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：DASHSCOPE_API_KEY = "sk-xxx" DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY") headers = { "Authorization": f"Bearer {DASHSCOPE_API_KEY}", "Content-Type": "application/json", "X-DashScope-Async": "enable" } payload = { "model": "qwen3-asr-flash-filetrans", "input": { "file_url": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" }, "parameters": { "channel_id": [0], # "language": "zh", "enable_itn": False # "corpus": { # "text": "" # } } } response = requests.post(url, headers=headers, data=json.dumps(payload)) if response.status_code == 200: print(f"task_id: {response.json()["output"]["task_id"]}") else: print("task failed!") print(response.json()) ``` |
| --- | --- |
| **model** `*string*` **（必选）** [模型](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#b8c8c0483153o)名称。仅适用于千问3-ASR-Flash-Filetrans模型。 |
| **input** `*object*` **（必选）** **属性** **file\\_url** `*string*`**（必选）** 待识别音频文件URL，URL必须公网可访问。 使用SDK时，若录音文件存储在[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/simple-upload#a632b50f190j8)，不支持使用以 `oss://`为前缀的临时 URL。 使用RESTful API时，若录音文件存储在[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/simple-upload#a632b50f190j8)，支持使用以 `oss://`为前缀的临时 URL。但需注意： **重要** - 临时 URL 有效期48小时，过期后无法使用，**请勿用于生产环境。** - 文件上传凭证接口限流为 100 QPS 且不支持扩容，**请勿用于生产环境、高并发及压测场景。** - 生产环境建议使用[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/what-is-oss) 等稳定存储，确保文件长期可用并规避限流问题。 |
| **parameters** `*object*` （可选） **属性** **language** *string*（可选）无默认值 若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率。 只能指定一个语种。 若音频语种不确定，或包含多种语种（例如中英日韩混合），请勿指定该参数。 **取值范围** - zh：中文（普通话、四川话、闽南语、吴语） - yue：粤语 - en：英文 - ja：日语 - de：德语 - ko：韩语 - ru：俄语 - fr：法语 - pt：葡萄牙语 - ar：阿拉伯语 - it：意大利语 - es：西班牙语 - hi：印地语 - id：印尼语 - th：泰语 - tr：土耳其语 - uk：乌克兰语 - vi：越南语 - cs：捷克语 - da：丹麦语 - fil：菲律宾语 - fi：芬兰语 - is：冰岛语 - ms：马来语 - no：挪威语 - pl：波兰语 - sv：瑞典语 **enable\\_itn** `*boolean*`（可选）默认值为`false` 是否启用ITN（Inverse Text Normalization，逆文本标准化）。该功能仅适用于中文和英文音频。 参数值： - true：开启； - false：关闭。 **enable\\_words** `*boolean*` （可选）默认值为`false` 控制是否返回字级别时间戳： - `false`：返回句级时间戳 - `true`：返回字级时间戳 字级别时间戳仅支持以下语种：中文、英语、日语、韩语、德语、法语、西班牙语、意大利语、葡萄牙语、俄语，其他语种可能无法保证准确性 同时，该参数还影响断句规则： - `false`：基于 VAD（语音活动检测）断句 - `true`：基于 VAD + 标点符号断句 **channel\\_id** `*array*` （可选）默认值为`[0]` 指定在多音轨音频文件中需要识别的音轨索引，索引从 0 开始。例如，\\[0\\] 表示识别第一个音轨，\\[0, 1\\] 表示同时识别第一和第二个音轨。如果省略此参数，则默认处理第一个音轨。 **重要** 指定的每一个音轨都将独立计费。例如，为单个文件请求 \\[0, 1\\] 会产生两笔独立的费用。 |

| #### **返回体** | ``` { "request_id": "92e3decd-0c69-47a8-************", "output": { "task_id": "8fab76d0-0eed-4d20-************", "task_status": "PENDING" } } ``` |
| --- | --- |
| **request\\_id** `*string*` 本次调用的唯一标识符。 |
| **output** `*object*` 调用结果信息。 **属性** **task\\_id** `*string*` 任务ID。该ID在查询语音识别任务接口中作为请求参数传入。 **task\\_status** `*string*` 任务状态： - PENDING：任务排队中 - RUNNING：任务处理中 - SUCCEEDED：任务执行成功 - FAILED：任务执行失败 - UNKNOWN：任务不存在或状态未知 |

### **获取任务执行结果**

#### **URL**

## 中国内地

HTTP请求地址：`GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}`

SDK调用配置的base\_url：`https://dashscope.aliyuncs.com/api/v1`

## 国际

HTTP请求地址：`GET https://dashscope-intl.aliyuncs.com/api/v1/tasks/{task_id}`

SDK调用配置的base\_url：`https://dashscope-intl.aliyuncs.com/api/v1`

| #### **请求体** | ## cURL ``` # ======= 重要提示 ======= # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/tasks/{task_id}，注意，将{task_id}替换为待查询任务ID # 新加坡地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # === 执行时请删除该注释 === curl --location --request GET 'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}' \\ --header "Authorization: Bearer $DASHSCOPE_API_KEY" \\ --header "X-DashScope-Async: enable" \\ --header "Content-Type: application/json" ``` ## Java SDK示例请参见[快速开始](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#7818a3bc466d6)。 ``` import okhttp3.*; import java.io.IOException; public class Main { public static void main(String[] args) { // 替换为实际的task_id String taskId = "xxx"; // 新加坡地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key // 若没有配置环境变量，请用百炼API Key将下行替换为：String apiKey = "sk-xxx" String apiKey = System.getenv("DASHSCOPE_API_KEY"); // 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/tasks/{task_id}，注意，将{task_id}替换为待查询任务ID String apiUrl = "https://dashscope.aliyuncs.com/api/v1/tasks/" + taskId; OkHttpClient client = new OkHttpClient(); Request request = new Request.Builder() .url(apiUrl) .addHeader("Authorization", "Bearer " + apiKey) .addHeader("X-DashScope-Async", "enable") .addHeader("Content-Type", "application/json") .get() .build(); try (Response response = client.newCall(request).execute()) { if (response.body() != null) { System.out.println(response.body().string()); } } catch (IOException e) { e.printStackTrace(); } } } ``` ## Python SDK示例请参见[快速开始](https://help.aliyun.com/zh/model-studio/qwen-speech-recognition#7818a3bc466d6)。 ``` import os import requests # 新加坡地域和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：DASHSCOPE_API_KEY = "sk-xxx" DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY") # 替换为实际的task_id task_id = "xxx" # 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1/tasks/{task_id}，注意，将{task_id}替换为待查询任务ID url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}" headers = { "Authorization": f"Bearer {DASHSCOPE_API_KEY}", "X-DashScope-Async": "enable", "Content-Type": "application/json" } response = requests.get(url, headers=headers) print(response.json()) ``` |
| --- | --- |
| **task\\_id** `*string*` **（必选）** 任务ID。将[提交任务](#88657039c4x0g)返回结果中的task\\_id作为参数传入，查询语音识别结果。 |

| #### **返回体** | ## RUNNING ``` { "request_id": "6769df07-2768-4fb0-ad59-************", "output": { "task_id": "9be1700a-0f8e-4778-be74-************", "task_status": "RUNNING", "submit_time": "2025-10-27 14:19:31.150", "scheduled_time": "2025-10-27 14:19:31.233", "task_metrics": { "TOTAL": 1, "SUCCEEDED": 0, "FAILED": 0 } } } ``` ## SUCCEEDED ``` { "request_id": "1dca6c0a-0ed1-4662-aa39-************", "output": { "task_id": "8fab76d0-0eed-4d20-929f-************", "task_status": "SUCCEEDED", "submit_time": "2025-10-27 13:57:45.948", "scheduled_time": "2025-10-27 13:57:46.018", "end_time": "2025-10-27 13:57:47.079", "result": { "transcription_url": "http://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/pre/pre-funasr-mlt-v1/20251027/13%3A57/7a3a8236-ffd1-4099-a280-0299686ac7da.json?Expires=1761631066&OSSAccessKeyId=LTAI**************&Signature=1lKv4RgyWCarRuUdIiErOeOBnwM%3D&response-content-disposition=attachment%3Bfilename%3D7a3a8236-ffd1-4099-a280-0299686ac7da.json" } }, "usage": { "seconds": 3 } } ``` ## FAILED ``` { "request_id": "3d141841-858a-466a-9ff9-************", "output": { "task_id": "c58c7951-7789-4557-9ea3-************", "task_status": "FAILED", "submit_time": "2025-10-27 15:06:06.915", "scheduled_time": "2025-10-27 15:06:06.967", "end_time": "2025-10-27 15:06:07.584", "code": "FILE_403_FORBIDDEN", "message": "FILE_403_FORBIDDEN" } } ``` |
| --- | --- |
| **request\\_id** `*string*` 本次调用的唯一标识符。 |
| **output** `*object*` 调用结果信息。 **属性** **task\\_id** `*string*` 任务ID。该ID在查询语音识别任务接口中作为请求参数传入。 **task\\_status** `*string*` 任务状态： - PENDING：任务排队中 - RUNNING：任务处理中 - SUCCEEDED：任务执行成功 - FAILED：任务执行失败 - UNKNOWN：任务不存在或状态未知 **result** `*object*` 语音识别结果。 **属性** **transcription\\_url** `*string*` 识别结果文件的下载 URL，链接有效期为 24 小时。过期后无法查询任务，也无法通过先前的 URL 下载结果。 识别结果以 JSON 文件保存，可通过该链接下载文件，或直接使用 HTTP 请求读取文件内容。 详情参见[异步调用识别结果说明](#2c27ad3e80p4y)。 **submit\\_time** `*string*` 任务提交时间。 **schedule\\_time** `*string*` 任务调度时间，即开始执行时间。 **end\\_time** `*string*` 任务结束时间。 **task\\_metrics** `*object*` 任务指标，包含子任务状态的统计信息。 **属性** **TOTAL** `*integer*` 子任务总数。 **SUCCEEDED** `*integer*` 子任务成功数。 **FAILED** `*integer*` 子任务失败数。 **code** `*string*` 错误码，仅在任务失败时返回。 **message** `*string*` 错误信息，仅任务失败时返回。 **usage** `*object*` 本次请求的Token消耗信息。 **属性** **seconds** `*integer*` 千问3-ASR-Flash音频时长（秒）。 |

| ### **异步调用识别结果说明** | ``` { "file_url": "https://***.mp3", "audio_info": { "format": "mp3", "sample_rate": 22050 }, "transcripts": [ { "channel_id": 0, "text": "欢迎使用阿里云。", "sentences": [ { "sentence_id": 0, "begin_time": 0, "end_time": 1440, "language": "zh", "emotion": "neutral", "text": "欢迎使用阿里云。", "words": [ { "begin_time": 0, "end_time": 160, "text": "欢", "punctuation": "" }, { "begin_time": 160, "end_time": 320, "text": "迎", "punctuation": "" }, { "begin_time": 320, "end_time": 640, "text": "使", "punctuation": "" }, { "begin_time": 640, "end_time": 720, "text": "用", "punctuation": "" }, { "begin_time": 880, "end_time": 960, "text": "阿", "punctuation": "" }, { "begin_time": 1040, "end_time": 1120, "text": "里", "punctuation": "" }, { "begin_time": 1120, "end_time": 1440, "text": "云", "punctuation": "。" } ] } ] } ] } ``` |
| --- | --- |
| **file\\_url** `*string*` 被识别的音频文件URL。 |
| **audio\\_info** `*object*` 被识别音频文件相关信息。 **属性** **format** `*string*` 音频格式。 **sample\\_rate** `*integer*` 音频采样率。 |
| **transcripts** `*array*` 完整的识别结果列表，每个元素对应一条音轨的识别内容。 **属性** **channel\\_id** `*integer*` 音轨索引，以0为起始。 **text** `*string*` 识别结果文本。 **sentences** `*object*` 句子级别的识别结果列表。 **属性** **begin\\_time**`*integer*` 句子开始时间戳（毫秒）。 **end\\_time**`*integer*` 句子结束时间戳（毫秒）。 **text** `*string*` 识别结果文本。 **sentence\\_id** `*integer*` 句子索引，以0为起始。 **language** `*string*` 被识别音频的语种。当请求参数`language`已指定语种时，该值与所指定的参数一致。 **取值范围** - zh：中文（普通话、四川话、闽南语、吴语） - yue：粤语 - en：英文 - ja：日语 - de：德语 - ko：韩语 - ru：俄语 - fr：法语 - pt：葡萄牙语 - ar：阿拉伯语 - it：意大利语 - es：西班牙语 - hi：印地语 - id：印尼语 - th：泰语 - tr：土耳其语 - uk：乌克兰语 - vi：越南语 - cs：捷克语 - da：丹麦语 - fil：菲律宾语 - fi：芬兰语 - is：冰岛语 - ms：马来语 - no：挪威语 - pl：波兰语 - sv：瑞典语 **emotion** `*string*` 被识别音频的情感。支持的情感如下： - `surprised`：惊讶 - `neutral`：平静 - `happy`：愉快 - `sad`：悲伤 - `disgusted`：厌恶 - `angry`：愤怒 - `fearful`：恐惧 **words** `*object*` 词级别的识别结果列表。当请求参数`enable_words`设为`true`时展示该结果。 **属性** **begin\\_time**`*integer*` 开始时间戳（毫秒）。 **end\\_time**`*integer*` 结束时间戳（毫秒）。 **text** `*string*` 识别结果文本。 **punctuation** `*string*` 标点符号。 |

.aliyun-docs-content .one-codeblocks pre { max-height: calc(80vh - 136px) !important; height: auto; } .tab-item { font-size: 12px !important; /\* 你可以根据需要调整字体大小 \*/ padding: 0px 5px !important; } .expandable-content { border-left: none !important; border-right: none !important; border-bottom: none !important; }

/\* 调整 table 宽度 \*/ .aliyun-docs-content table.medium-width { max-width: 1018px; width: 100%; } .aliyun-docs-content table.table-no-border tr td:first-child { padding-left: 0; } .aliyun-docs-content table.table-no-border tr td:last-child { padding-right: 0; } /\* 支持吸顶 \*/ div:has(.aliyun-docs-content), .aliyun-docs-content .markdown-body { overflow: visible; } .stick-top { position: sticky; top: 46px; } /\*\*代码块字体\*\*/ /\* 减少表格中的代码块 margin，让表格信息显示更紧凑 \*/ .unionContainer .markdown-body table .help-code-block { margin: 0 !important; } /\* 减少表格中的代码块字号，让表格信息显示更紧凑 \*/ .unionContainer .markdown-body .help-code-block pre { font-size: 12px !important; } /\* 减少表格中的代码块字号，让表格信息显示更紧凑 \*/ .unionContainer .markdown-body .help-code-block pre code { font-size: 12px !important; } /\*\* API Reference 表格 \*\*/ .aliyun-docs-content table.api-reference tr td:first-child { margin: 0px; border-bottom: 1px solid #d8d8d8; } .aliyun-docs-content table.api-reference tr:last-child td:first-child { border-bottom: none; } .aliyun-docs-content table.api-reference p { color: #6e6e80; } .aliyun-docs-content table.api-reference b, i { color: #181818; } .aliyun-docs-content table.api-reference .collapse { border: none; margin-top: 4px; margin-bottom: 4px; } .aliyun-docs-content table.api-reference .collapse .expandable-title-bold { padding: 0; } .aliyun-docs-content table.api-reference .collapse .expandable-title { padding: 0; } .aliyun-docs-content table.api-reference .collapse .expandable-title-bold .title { margin-left: 16px; } .aliyun-docs-content table.api-reference .collapse .expandable-title .title { margin-left: 16px; } .aliyun-docs-content table.api-reference .collapse .expandable-title-bold i.icon { position: absolute; color: #777; font-weight: 100; } .aliyun-docs-content table.api-reference .collapse .expandable-title i.icon { position: absolute; color: #777; font-weight: 100; } .aliyun-docs-content table.api-reference .collapse.expanded .expandable-content { padding: 10px 14px 10px 14px !important; margin: 0; border: 1px solid #e9e9e9; } .aliyun-docs-content table.api-reference .collapse .expandable-title-bold b { font-size: 13px; font-weight: normal; color: #6e6e80; } .aliyun-docs-content table.api-reference .collapse .expandable-title b { font-size: 13px; font-weight: normal; color: #6e6e80; } .aliyun-docs-content table.api-reference .tabbed-content-box { border: none; } .aliyun-docs-content table.api-reference .tabbed-content-box section { padding: 8px 0 !important; } .aliyun-docs-content table.api-reference .tabbed-content-box.mini .tab-box { /\* position: absolute; left: 40px; right: 0; \*/ } .aliyun-docs-content .margin-top-33 { margin-top: 33px !important; } .aliyun-docs-content .two-codeblocks pre { max-height: calc(50vh - 136px) !important; height: auto; } .expandable-content section { border-bottom: 1px solid #e9e9e9; padding-top: 6px; padding-bottom: 4px; } .expandable-content section:last-child { border-bottom: none; } .expandable-content section:first-child { padding-top: 0; }