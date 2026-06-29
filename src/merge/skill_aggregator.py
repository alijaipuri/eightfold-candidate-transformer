from collections import defaultdict

from src.models.skill import CanonicalSkill
from src.normalization.skill_normalizer import SkillNormalizer


class SkillAggregator:

    def __init__(self):
        self.normalizer = SkillNormalizer()

    def aggregate(
        self,
        parsed_sources: dict
    ) -> list[CanonicalSkill]:

        skill_sources = defaultdict(set)

        ats = parsed_sources.get("ats_json")

        if ats:
            for skill in ats.raw_data.get(
                "skills",
                []
            ):
                normalized = (
                    self.normalizer.normalize(
                        skill
                    )
                )

                skill_sources[
                    normalized
                ].add("ats_json")

        linkedin = parsed_sources.get(
            "linkedin_profile"
        )

        if linkedin:
            for skill in linkedin.raw_data.get(
                "skills",
                []
            ):
                normalized = (
                    self.normalizer.normalize(
                        skill
                    )
                )

                skill_sources[
                    normalized
                ].add(
                    "linkedin_profile"
                )

        github = parsed_sources.get(
            "github_profile"
        )

        if github:
            for skill in github.raw_data.get(
                "languages",
                []
            ):
                normalized = (
                    self.normalizer.normalize(
                        skill
                    )
                )

                skill_sources[
                    normalized
                ].add(
                    "github_profile"
                )

        skills = []

        for skill, sources in (
            skill_sources.items()
        ):

            confidence = min(
                0.70
                +
                (
                    len(sources)
                    * 0.08
                ),
                1.0
            )

            skills.append(
                CanonicalSkill(
                    skill_name=skill,
                    confidence=confidence,
                    supporting_sources=list(
                        sources
                    ),
                    occurrence_count=len(
                        sources
                    )
                )
            )

        skills.sort(
            key=lambda x: (
                x.confidence,
                x.occurrence_count
            ),
            reverse=True
        )

        return skills
