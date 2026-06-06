import os
import re
from pathlib import Path

def fix_math_delimiters(directory):
    dir_path = Path(directory)
    
    # 匹配 "Day [x] Fixed.md" 的正则表达式，其中 x 是一个或多个数字
    pattern = re.compile(r'^Day \d+ Fixed\.md$')
    
    # 使用 rglob 递归遍历目录下的所有 .md 文件
    count = 0
    for md_file in dir_path.rglob('Day * Fixed.md'):
        if pattern.match(md_file.name):
            print(f"正在处理: {md_file}")
            
            # 读取文件内容
            try:
                content = md_file.read_text(encoding='utf-8')
            except Exception as e:
                print(f"读取文件失败 '{md_file}': {e}")
                continue
            
            # 替换行间公式块 \[ \] 为 $$ $$
            content = content.replace(r'\[', '$$')
            content = content.replace(r'\]', '$$')
            
            # 替换行内公式 \( \) 为 $ $
            content = content.replace(r'\(', '$')
            content = content.replace(r'\)', '$')
            
            # 写回文件
            try:
                md_file.write_text(content, encoding='utf-8')
                count += 1
            except Exception as e:
                print(f"保存文件失败 '{md_file}': {e}")
                
    print(f"\n处理完成！共修改了 {count} 个文件。")

if __name__ == "__main__":
    import sys

    target_dir = r"output"
        
    print(f"目标目录: {os.path.abspath(target_dir)}")
    fix_math_delimiters(target_dir)