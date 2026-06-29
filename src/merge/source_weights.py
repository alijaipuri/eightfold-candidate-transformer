from enum import Enum


class SourceType(str, Enum):
    RECRUITER_CSV = "recruiter_csv"
    ATS_JSON = "ats_json"
    LINKEDIN = "linkedin_profile"
    GITHUB = "github_profile"
    RESUME = "resume"
    RECRUITER_NOTES = "recruiter_notes"


SOURCE_CONFIDENCE_WEIGHTS = {
    SourceType.RECRUITER_CSV: 0.95,
    SourceType.ATS_JSON: 0.92,
    SourceType.LINKEDIN: 0.90,
    SourceType.GITHUB: 0.82,
    SourceType.RESUME: 0.80,
    SourceType.RECRUITER_NOTES: 0.65,
}
