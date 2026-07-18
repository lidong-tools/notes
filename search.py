#!/usr/bin/env python3
"""混合检索 ~/seo-notes 知识库：语义 (BGE) + 关键词 (BM25)"""

import os, sys, json
from pathlib import Path

NOTES_DIR = Path.home() / "seo-notes"
INDEX_DIR = Path.home() / ".seo_index"

os.environ.setdefault("HF_HUB_OFFLINE", "1")

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import jieba

N = int(sys.argv[2]) if len(sys.argv) > 2 else 5
QUERY = sys.argv[1] if len(sys.argv) > 1 else None

if not QUERY:
    print("用法: search.py \"关键词\" [-n 返回条数]")
    sys.exit(1)


def tokenize(text):
    return list(jieba.cut(text))


def search():
    client = chromadb.PersistentClient(path=str(INDEX_DIR / "chroma"),
                                       settings=Settings(anonymized_telemetry=False))
    try:
        coll = client.get_collection("seo_notes")
    except Exception:
        print("❌ 索引不存在，请先运行 build_index.py")
        sys.exit(1)

    # 语义检索（取更多候选给 BM25 混合排序）
    print(f"🔍 搜索: {QUERY}\n")
    model = SentenceTransformer("BAAI/bge-base-zh-v1.5")
    q_embed = model.encode([QUERY], normalize_embeddings=True)
    results = coll.query(query_embeddings=q_embed.tolist(), n_results=min(N * 3, coll.count()))

    if not results["documents"][0]:
        print("😕 没有找到相关结果")
        return

    # BM25 关键词重排
    docs = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    tokenized_docs = [tokenize(d) for d in docs]
    bm25 = BM25Okapi(tokenized_docs)
    q_tokens = tokenize(QUERY)
    bm25_scores = bm25.get_scores(q_tokens)

    # 混合：语义分 + BM25 分
    max_bm25 = max(bm25_scores) if bm25_scores.max() > 0 else 1
    combined = []
    for i, (doc, meta, dist) in enumerate(zip(docs, metadatas, distances)):
        sem_score = 1.0 - dist  # distance → similarity
        kw_score = bm25_scores[i] / max_bm25
        combined.append((sem_score * 0.6 + kw_score * 0.4, doc, meta))

    combined.sort(reverse=True, key=lambda x: x[0])

    for rank, (score, doc, meta) in enumerate(combined[:N], 1):
        path = meta.get("path", "?")
        preview = doc[:150].replace("\n", " ")
        print(f"#{rank} 📄 {path}  (score: {score:.3f})")
        print(f"    {preview}...")
        print()


if __name__ == "__main__":
    search()
