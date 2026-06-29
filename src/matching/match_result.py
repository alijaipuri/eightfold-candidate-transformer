from typing import Dict, List

from pydantic import BaseModel, Field


class MatchEvidence(BaseModel):
    attribute: str
    source_a: str
    source_b: str
    value_a: str
    value_b: str
    similarity_score: float


class MatchResult(BaseModel):
    candidate_match: bool

    overall_score: float = Field(
        ge=0.0,
        le=1.0
    )

    confidence_level: str

    evidences: List[MatchEvidence]

    weighted_breakdown: Dict[str, float]
