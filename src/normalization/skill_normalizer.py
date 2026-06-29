from typing import Optional

from src.normalization.base import BaseNormalizer


class SkillNormalizer(BaseNormalizer):

    SKILL_MAP = {
        "ml": "Machine Learning",
        "machine learning": "Machine Learning",
        "machine-learning": "Machine Learning",
        "ai": "Artificial Intelligence",
        "postgres": "PostgreSQL",
        "postgresql": "PostgreSQL",
        "js": "JavaScript",
    }

    def normalize(
        self,
        value: Optional[str]
    ) -> Optional[str]:

        if not value:
            return None

        skill = value.strip().lower()

        return self.SKILL_MAP.get(
            skill,
            value.strip()
        )
