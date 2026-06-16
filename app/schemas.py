"""
Pydantic schemas for request and response validation
"""
from pydantic import BaseModel, Field
from typing import Optional, List


class CitationSource(BaseModel):
    """Citation source for an answer."""
    document: str = Field(..., description="Document name (e.g., insurance_claims.md)")
    section: Optional[str] = Field(None, description="Section of document")
    chunk_id: Optional[str] = Field(None, description="Chunk identifier")


class QuestionRequest(BaseModel):
    """Request model for asking a question."""
    question: str = Field(..., description="User question about healthcare policies")
    top_k: int = Field(4, ge=1, le=10, description="Number of retrieved chunks to use")


class QuestionResponse(BaseModel):
    """Response model for a question."""
    answer: str = Field(..., description="Generated answer grounded in documents")
    citations: List[CitationSource] = Field(default_factory=list, description="Sources for the answer")
    confidence: str = Field("medium", description="Confidence level: high, medium, low")
    escalation_note: Optional[str] = Field(None, description="Note for human review if confidence is low")


class DocumentInfo(BaseModel):
    """Information about an ingested document."""
    name: str = Field(..., description="Document name")
    path: str = Field(..., description="File path")
    chunks: int = Field(..., description="Number of chunks created")
    size_kb: float = Field(..., description="File size in KB")


class IngestResponse(BaseModel):
    """Response from document ingestion."""
    status: str = Field(..., description="Status of ingestion (success, error)")
    documents_ingested: int = Field(..., description="Number of documents ingested")
    total_chunks: int = Field(..., description="Total chunks created")
    documents: List[DocumentInfo] = Field(default_factory=list)
    error: Optional[str] = Field(None, description="Error message if ingestion failed")


class HealthCheckResponse(BaseModel):
    """Health check response."""
    status: str = Field(..., description="Service status")
    service: str = Field(..., description="Service name")
    version: str = Field(..., description="Service version")
