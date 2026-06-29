from typing import List, Optional
from pydantic import BaseModel, Field


class ProvenanceRecord(BaseModel):
    source: str
    method: str


class SkillEntry(BaseModel):
    name: str
    confidence: float = Field(ge=0.0, le=1.0)
    sources: List[str]


class ExperienceEntry(BaseModel):
    company: str
    title: str
    start: Optional[str] = None
    end: Optional[str] = None
    summary: Optional[str] = None


class EducationEntry(BaseModel):
    institution: str
    degree: Optional[str] = None
    field: Optional[str] = None
    end_year: Optional[int] = None


class LocationEntry(BaseModel):
    city: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None


class LinksEntry(BaseModel):
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None
    other: List[str] = []
