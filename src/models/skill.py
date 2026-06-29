from typing import List

from pydantic import BaseModel, Field


class CanonicalSkill(BaseModel):
    skill_name: str

    confidence: float = Field(
        ge=0.0,
        le=1.0
    )

    supporting_sources: List[str]

    occurrence_count: int
