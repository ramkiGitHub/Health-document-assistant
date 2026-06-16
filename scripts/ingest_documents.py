"""Ingestion script: load markdown files, chunk them, and write processed JSON files.

Run from the project root:

    python scripts/ingest_documents.py

"""
import json
import sys
from pathlib import Path

# Ensure project root is on sys.path so imports like `app.rag` work when running
# this script directly (e.g., `python scripts/ingest_documents.py`).
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.rag.loaders import load_markdown_files
from app.rag.splitter import create_chunks_for_document
from app.config import config


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def main():
    data_path = Path(config.DATA_PATH)
    processed_dir = Path("data/processed")
    ensure_dir(processed_dir)

    docs = load_markdown_files(str(data_path))
    total_docs = len(docs)
    total_chunks = 0

    for doc in docs:
        doc_name = doc["document_name"]
        chunks = create_chunks_for_document(doc_name, doc["text"], chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
        total_chunks += len(chunks)
        out_file = processed_dir / f"{doc_name}.chunks.json"
        with out_file.open("w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=2, ensure_ascii=False)
        print(f"Wrote {len(chunks)} chunks for {doc_name} -> {out_file}")

    print(f"Processed {total_docs} documents with {total_chunks} total chunks.")


if __name__ == "__main__":
    main()
