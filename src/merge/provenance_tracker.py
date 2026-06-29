from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProvenanceEntry(BaseModel):
    field_name: str
    selected_value: str
    selected_source: str
    source_confidence: float
    competing_values: List[str]
    resolution_strategy: str
    resolved_at: datetime = datetime.utcnow()
