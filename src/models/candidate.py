from typing import Dict, List, Optional

from pydantic import BaseModel

from src.models.common import (
    EducationEntry,
    ExperienceEntry,
    LinksEntry,
    LocationEntry,
    ProvenanceRecord,
    SkillEntry,
)


class CandidateProfile(BaseModel):
    candidate_id: str

    full_name: Optional[str] = None

    emails: List[str] = []

    phones: List[str] = []

    location: Optional[LocationEntry] = None

    links: Optional[LinksEntry] = None

    headline: Optional[str] = None

    years_experience: Optional[float] = None

    skills: List[SkillEntry] = []

    experience: List[ExperienceEntry] = []

    education: List[EducationEntry] = []

    provenance: Dict[str, ProvenanceRecord] = {}

    overall_confidence: float = 0.0
