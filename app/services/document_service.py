"""Document service helpers for file listing and ingestion."""
from pathlib import Path
from typing import List

from app.schemas import DocumentInfo


def _find_text_documents(data_path: str) -> List[Path]:
    path = Path(data_path)
    if not path.exists() or not path.is_dir():
        return []
    return sorted([p for p in path.glob("*.md") if p.is_file()])


def _estimate_chunk_count(text: str, chunk_size: int = 800) -> int:
    if not text:
        return 0
    return max(1, (len(text) + chunk_size - 1) // chunk_size)


def list_documents(data_path: str) -> List[DocumentInfo]:
    documents: List[DocumentInfo] = []
    for path in _find_text_documents(data_path):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            text = ""

        documents.append(
            DocumentInfo(
                name=path.name,
                path=str(path),
                chunks=_estimate_chunk_count(text),
                size_kb=round(path.stat().st_size / 1024, 2),
            )
        )

    return documents


def ingest_documents(data_path: str):
    documents = list_documents(data_path)
    total_chunks = sum(document.chunks for document in documents)
    return documents, total_chunks
