"""Simple text splitter for chunking documents with overlap."""
from typing import List, Dict


def chunk_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    """Split text into chunks by characters with a fixed overlap.

    This is a simple splitter intended for Phase 2. It preserves raw text and
    returns a list of chunk strings.
    """
    if not text:
        return []

    text = text.strip()
    chunks: List[str] = []
    start = 0
    N = len(text)
    if chunk_size <= 0:
        return [text]

    while start < N:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        if end >= N:
            break
        start = end - chunk_overlap
        if start < 0:
            start = 0

    return chunks


def create_chunks_for_document(document_name: str, text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Dict]:
    """Create chunk metadata dicts for a document.

    Each chunk dict contains:
    - chunk_id
    - document_name
    - text
    - index
    """
    raw_chunks = chunk_text(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    result: List[Dict] = []
    for i, c in enumerate(raw_chunks, start=1):
        result.append({
            "chunk_id": f"{document_name}__{i:04d}",
            "document_name": document_name,
            "index": i,
            "text": c,
        })

    return result
