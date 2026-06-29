from typing import List, Optional

from pydantic import BaseModel


class FieldProjection(BaseModel):
    path: str
    from_field: str
    required: bool = False
    normalize: Optional[str] = None


class ProjectionConfig(BaseModel):
    fields: List[FieldProjection]
    include_confidence: bool = True
    on_missing: str = "null"
