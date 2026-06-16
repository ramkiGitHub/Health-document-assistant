"""Quick test script using FastAPI TestClient to call endpoints locally without starting a server."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from fastapi.testclient import TestClient
from main import app


def main():
    client = TestClient(app)
    resp = client.get("/documents/processed")
    print("status_code:", resp.status_code)
    try:
        print(resp.json()[:2])
    except Exception:
        print(resp.text)


if __name__ == "__main__":
    main()
