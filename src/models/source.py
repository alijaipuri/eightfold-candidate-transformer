from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class SourceMetadata(BaseModel):
    source_name: str
    file_path: str
    ingestion_timestamp: datetime = Field(
        default_factory=datetime.utcnow
    )
    record_count: int = 1


class SourcePayload(BaseModel):
    metadata: SourceMetadata
    raw_data: Any
