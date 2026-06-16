"""Question-answering service for Phase 1 mock responses."""
from typing import List, Optional, Tuple

from app.schemas import CitationSource


def generate_mock_answer(question: str, top_k: int = 4) -> Tuple[str, List[CitationSource], str, Optional[str]]:
    normalized = question.strip().lower()
    medical_trigger = ["medical advice", "diagnose", "should i", "what should i do", "treatment"]
    if any(trigger in normalized for trigger in medical_trigger):
        return (
            "I cannot provide medical advice from the current synthetic documents. Please consult a qualified healthcare professional.",
            [
                CitationSource(
                    document="patient_privacy.md",
                    section="Patient Rights",
                    chunk_id="patient_privacy_001",
                )
            ],
            "low",
            "This request appears clinical and should be reviewed by a human reviewer.",
        )

    return (
        "This is a placeholder answer for Phase 1. The assistant will use the document retrieval pipeline in later phases to generate grounded responses.",
        [
            CitationSource(
                document="insurance_claims.md",
                section="Required Documents",
                chunk_id="insurance_claims_001",
            )
        ],
        "high",
        None,
    )
