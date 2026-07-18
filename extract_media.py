"""
从知识库 MD 文件中提取媒体资源：原文链接 + OSS 图片下载到本地。
用法: python3 extract_media.py <md_file_path> [--max-images N]
输出: JSON，包含 source_url, images (本地路径列表)
"""
import sys
import re
import json
import os
import urllib.request
from pathlib import Path

MAX_IMAGES = 3  # 默认最多下载图片数
CACHE_DIR = "/tmp/hermes-kb-images"


def extract_images(md_path: str, max_images: int = MAX_IMAGES) -> dict:
    """从 MD 文件中提取图片链接并下载到本地"""
    result = {"source_url": "", "github_url": "", "images": [], "image_urls": []}

    os.makedirs(CACHE_DIR, exist_ok=True)

    # 计算 GitHub blob 链接
    repo_base = os.path.dirname(os.path.abspath(__file__))
    abs_md = os.path.abspath(md_path)
    rel_path = os.path.relpath(abs_md, repo_base)
    result["github_url"] = f"https://github.com/lidong-tools/notes/blob/main/{rel_path}"

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 提取 source 链接（frontmatter）
    source_match = re.search(r'source:\s*"([^"]+)"', content)
    if source_match:
        result["source_url"] = source_match.group(1)

    # 提取所有 OSS 图片链接（URL 路径中可能有括号，所以匹配到图片扩展名为止）
    pattern = re.compile(r'https://ima-knowledge\.oss-cn-shanghai\.aliyuncs\.com/\S+?\.(?:webp|png|jpg|jpeg|gif|svg)')
    matches = pattern.findall(content)

    downloaded = 0
    for url in matches:
        if downloaded >= max_images:
            break

        # 从URL提取文件名
        filename = url.split("/")[-1]
        # 处理 URL 编码
        local_path = os.path.join(CACHE_DIR, filename)

        # 跳过已下载的
        if os.path.exists(local_path):
            result["images"].append(local_path)
            result["image_urls"].append(url)
            downloaded += 1
            continue

        try:
            urllib.request.urlretrieve(url, local_path)
            result["images"].append(local_path)
            result["image_urls"].append(url)
            downloaded += 1
        except Exception as e:
            print(f"  ⚠️ 下载失败: {filename}: {e}", file=sys.stderr)

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "用法: extract_media.py <md_file_path> [--max-images N]"}))
        sys.exit(1)

    md_path = sys.argv[1]
    max_images = MAX_IMAGES

    for i, arg in enumerate(sys.argv):
        if arg == "--max-images" and i + 1 < len(sys.argv):
            max_images = int(sys.argv[i + 1])

    if not os.path.exists(md_path):
        print(json.dumps({"error": f"文件不存在: {md_path}"}))
        sys.exit(1)

    result = extract_images(md_path, max_images)
    print(json.dumps(result, ensure_ascii=False))
