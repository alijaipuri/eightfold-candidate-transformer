from typing import List, Optional

from pydantic import BaseModel, Field

from src.models.skill import CanonicalSkill


class CanonicalField(BaseModel):
    """
    Represents a resolved canonical value for a candidate attribute,
    along with confidence and provenance information.
    """

    value: Optional[str]

    confidence: float = Field(
        ge=0.0,
        le=1.0
    )

    selected_source: Optional[str]

    supporting_sources: List[str] = []

    alternatives: List[str] = []


class CanonicalCandidate(BaseModel):
    """
    Unified candidate representation generated after
    entity resolution and conflict resolution.
    """

    candidate_id: str

    full_name: CanonicalField

    primary_email: CanonicalField

    primary_phone: CanonicalField

    current_company: CanonicalField

    current_title: CanonicalField

    skills: List[CanonicalSkill] = []
