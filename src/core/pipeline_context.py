from pathlib import Path
from typing import Optional

from pydantic import BaseModel


class PipelineContext(BaseModel):
    recruiter_csv: Optional[Path] = None
    ats_json: Optional[Path] = None
    github_profile: Optional[Path] = None
    linkedin_profile: Optional[Path] = None
    resume_file: Optional[Path] = None
    recruiter_notes: Optional[Path] = None
