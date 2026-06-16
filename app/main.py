"""
Healthcare Document Assistant - Main FastAPI Application
"""
from typing import List
from pathlib import Path

from fastapi import FastAPI

from .config import config
from .schemas import (
    DocumentInfo,
    HealthCheckResponse,
    IngestResponse,
    QuestionRequest,
    QuestionResponse,
)
from .services.document_service import ingest_documents, list_documents, list_processed_chunks
from .schemas import ChunkInfo
from .services.qa_service import generate_mock_answer

app = FastAPI(
    title="Healthcare Document Assistant",
    description="A GenAI MVP for asking questions over synthetic healthcare documents",
    version="0.1.0",
)


@app.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """Health check endpoint for monitoring."""
    return HealthCheckResponse(
        status="healthy",
        service="Healthcare Document Assistant",
        version="0.1.0",
    )


@app.get("/", response_model=dict)
async def root():
    """Welcome endpoint."""
    return {
        "message": "Welcome to Healthcare Document Assistant",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/documents", response_model=List[DocumentInfo])
async def documents():
    """List available synthetic healthcare documents."""
    return list_documents(config.DATA_PATH)


@app.get("/documents/processed", response_model=List[ChunkInfo])
async def documents_processed():
    """Return processed chunks for explainability (reads `data/processed`)."""
    processed_dir = Path("data/processed")
    chunks = list_processed_chunks(str(processed_dir))
    return chunks


@app.post("/documents/ingest", response_model=IngestResponse)
async def ingest():
    """Trigger a document ingestion preview for the current data folder."""
    documents, total_chunks = ingest_documents(config.DATA_PATH)
    return IngestResponse(
        status="success",
        documents_ingested=len(documents),
        total_chunks=total_chunks,
        documents=documents,
    )


@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """Ask a question and receive a mock answer with citations."""
    answer, citations, confidence, escalation_note = generate_mock_answer(
        question=request.question,
        top_k=request.top_k,
    )
    return QuestionResponse(
        answer=answer,
        citations=citations,
        confidence=confidence,
        escalation_note=escalation_note,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
