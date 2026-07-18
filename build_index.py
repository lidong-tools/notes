#!/usr/bin/env python3
"""增量/全量构建 ~/seo-notes 知识库的 ChromaDB 向量索引"""

import os, sys, json, subprocess
from pathlib import Path

NOTES_DIR = Path.home() / "seo-notes"
INDEX_DIR = Path.home() / ".seo_index"
INDEX_DIR.mkdir(parents=True, exist_ok=True)
LAST_COMMIT_FILE = INDEX_DIR / "last_commit"

# 离线模式
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

FORCE = "--force" in sys.argv


def get_current_head():
    r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=NOTES_DIR,
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def get_last_commit():
    if LAST_COMMIT_FILE.exists():
        return LAST_COMMIT_FILE.read_text().strip()
    return None


def get_changed_files():
    """获取自上次索引以来变更的 .md 文件"""
    last = get_last_commit()
    head = get_current_head()
    if not head:
        return []
    if not last:
        # 首次建索引：全部文件
        return sorted(NOTES_DIR.rglob("*.md"))
    if last == head:
        return []

    r = subprocess.run(
        ["git", "-c", "core.quotepath=false", "diff", "--name-only",
         "--diff-filter=AM", f"{last}..{head}"],
        cwd=NOTES_DIR, capture_output=True, text=True
    )
    changed = []
    for line in r.stdout.strip().split("\n"):
        path = NOTES_DIR / line
        if line and path.suffix == ".md" and path.exists():
            changed.append(path)
    return changed


def read_md(path):
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def build_index():
    files = get_changed_files() if not FORCE else sorted(NOTES_DIR.rglob("*.md"))

    if not files:
        print("✅ 没有新文件，索引无需更新")
        return

    print(f"🔨 {'全量' if FORCE else '增量'}索引 {len(files)} 个文件...")

    # 加载模型
    print("⏳ 加载 BGE 模型...")
    model = SentenceTransformer("BAAI/bge-base-zh-v1.5")
    print("✅ 模型就绪")

    # ChromaDB
    client = chromadb.PersistentClient(path=str(INDEX_DIR / "chroma"),
                                       settings=Settings(anonymized_telemetry=False))
    coll = client.get_or_create_collection(name="seo_notes")

    # 删除变更文件对应的旧向量（增量时）
    if not FORCE and get_last_commit():
        old_ids = [p.stem for p in files]
        try:
            coll.delete(ids=old_ids)
        except Exception:
            pass

    batch_docs, batch_ids, batch_metas = [], [], []
    for f in files:
        content = read_md(f)
        if not content.strip():
            continue
        fid = f.stem
        batch_docs.append(content[:2000])  # 截断长文
        batch_ids.append(fid)
        batch_metas.append({"path": str(f.relative_to(NOTES_DIR)), "filename": f.name})

        if len(batch_docs) >= 20:
            embeddings = model.encode(batch_docs, normalize_embeddings=True)
            coll.upsert(ids=batch_ids, embeddings=embeddings.tolist(),
                        documents=batch_docs, metadatas=batch_metas)
            batch_docs, batch_ids, batch_metas = [], [], []

    if batch_docs:
        embeddings = model.encode(batch_docs, normalize_embeddings=True)
        coll.upsert(ids=batch_ids, embeddings=embeddings.tolist(),
                    documents=batch_docs, metadatas=batch_metas)

    # 记录 commit
    head = get_current_head()
    if head:
        LAST_COMMIT_FILE.write_text(head)

    print(f"✅ 索引完成: {coll.count()} 篇文档")


if __name__ == "__main__":
    build_index()
