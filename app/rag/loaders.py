"""Document loaders for synthetic healthcare documents."""
from pathlib import Path
from typing import List, Dict


def load_markdown_files(data_path: str) -> List[Dict]:
    """Load all markdown files from `data_path` and return list of dicts.

    Each dict contains:
    - document_name
    - source_path
    - text
    """
    p = Path(data_path)
    if not p.exists() or not p.is_dir():
        return []

    docs: List[Dict] = []
    for fp in sorted(p.glob("*.md")):
        try:
            text = fp.read_text(encoding="utf-8")
        except Exception:
            text = ""
        docs.append({
            "document_name": fp.name,
            "source_path": str(fp),
            "text": text,
        })

    return docs
