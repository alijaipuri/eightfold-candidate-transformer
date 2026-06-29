from pydantic import BaseModel, Field


class FieldEvidence(BaseModel):
    source: str
    value: str
    source_confidence: float = Field(
        ge=0.0,
        le=1.0
    )
