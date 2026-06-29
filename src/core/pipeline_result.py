from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel


class PipelineResult(BaseModel):
    success: bool

    execution_timestamp: datetime

    processed_sources: List[str]

    warnings: List[str]

    canonical_profile: Dict[str, Any]

    provenance: Dict[str, Any]
