from pydantic import BaseModel
from typing import List


class ProjectionConfig(BaseModel):
    fields: List[str]
