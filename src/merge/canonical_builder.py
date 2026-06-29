from uuid import uuid4
from typing import Dict, List, Optional

from src.merge.field_evidence import FieldEvidence
from src.merge.field_resolver import FieldResolver
from src.merge.skill_aggregator import SkillAggregator
from src.merge.source_weights import SOURCE_CONFIDENCE_WEIGHTS

from src.models.canonical import CanonicalCandidate

from src.normalization.email_normalizer import EmailNormalizer
from src.normalization.phone_normalizer import PhoneNormalizer
from src.normalization.name_normalizer import NameNormalizer


class CanonicalCandidateBuilder:
    """
    Responsible for constructing a unified candidate profile
    from multiple heterogeneous candidate sources.
    """

    def __init__(self):

        self.field_resolver = FieldResolver()

        self.email_normalizer = EmailNormalizer()
        self.phone_normalizer = PhoneNormalizer()
        self.name_normalizer = NameNormalizer()

        self.skill_aggregator = SkillAggregator()

    def _create_evidence(
        self,
        source: str,
        value: Optional[str]
    ) -> Optional[FieldEvidence]:

        if value is None:
            return None

        value = value.strip()

        if not value:
            return None

        return FieldEvidence(
            source=source,
            value=value,
            source_confidence=
            SOURCE_CONFIDENCE_WEIGHTS[source]
        )

    def _collect_name_evidence(
        self,
        parsed_sources: Dict
    ) -> List[FieldEvidence]:

        evidences = []

        recruiter = parsed_sources.get("recruiter_csv")
        ats = parsed_sources.get("ats_json")
        linkedin = parsed_sources.get("linkedin_profile")
        github = parsed_sources.get("github_profile")

        candidates = [
            (
                "recruiter_csv",
                recruiter.raw_data[0].get("name")
                if recruiter else None
            ),
            (
                "ats_json",
                ats.raw_data.get("candidate_name")
                if ats else None
            ),
            (
                "linkedin_profile",
                linkedin.raw_data.get("full_name")
                if linkedin else None
            ),
            (
                "github_profile",
                github.raw_data.get("name")
                if github else None
            )
        ]

        for source, value in candidates:

            if value is None:
                continue

            normalized = (
                self.name_normalizer.normalize(
                    value
                )
            )

            evidence = self._create_evidence(
                source,
                normalized
            )

            if evidence:
                evidences.append(
                    evidence
                )

        return evidences

    def _collect_email_evidence(
        self,
        parsed_sources: Dict
    ) -> List[FieldEvidence]:

        evidences = []

        recruiter = parsed_sources.get(
            "recruiter_csv"
        )

        ats = parsed_sources.get(
            "ats_json"
        )

        candidates = [
            (
                "recruiter_csv",
                recruiter.raw_data[0].get("email")
                if recruiter else None
            ),
            (
                "ats_json",
                ats.raw_data.get(
                    "primary_email"
                )
                if ats else None
            )
        ]

        for source, value in candidates:

            normalized = (
                self.email_normalizer.normalize(
                    value
                )
            )

            evidence = self._create_evidence(
                source,
                normalized
            )

            if evidence:
                evidences.append(
                    evidence
                )

        return evidences

    def _collect_phone_evidence(
        self,
        parsed_sources: Dict
    ) -> List[FieldEvidence]:

        evidences = []

        recruiter = parsed_sources.get(
            "recruiter_csv"
        )

        ats = parsed_sources.get(
            "ats_json"
        )

        candidates = [
            (
                "recruiter_csv",
                recruiter.raw_data[0].get("phone")
                if recruiter else None
            ),
            (
                "ats_json",
                ats.raw_data.get(
                    "phone_number"
                )
                if ats else None
            )
        ]

        for source, value in candidates:

            normalized = (
                self.phone_normalizer.normalize(
                    value
                )
            )

            evidence = self._create_evidence(
                source,
                normalized
            )

            if evidence:
                evidences.append(
                    evidence
                )

        return evidences

    def _collect_company_evidence(
        self,
        parsed_sources: Dict
    ) -> List[FieldEvidence]:

        evidences = []

        recruiter = parsed_sources.get(
            "recruiter_csv"
        )

        ats = parsed_sources.get(
            "ats_json"
        )

        candidates = [
            (
                "recruiter_csv",
                recruiter.raw_data[0].get(
                    "current_company"
                )
                if recruiter else None
            ),
            (
                "ats_json",
                ats.raw_data.get(
                    "company"
                )
                if ats else None
            )
        ]

        for source, value in candidates:

            evidence = self._create_evidence(
                source,
                value
            )

            if evidence:
                evidences.append(
                    evidence
                )

        return evidences

    def _collect_title_evidence(
        self,
        parsed_sources: Dict
    ) -> List[FieldEvidence]:

        evidences = []

        recruiter = parsed_sources.get(
            "recruiter_csv"
        )

        ats = parsed_sources.get(
            "ats_json"
        )

        candidates = [
            (
                "recruiter_csv",
                recruiter.raw_data[0].get(
                    "title"
                )
                if recruiter else None
            ),
            (
                "ats_json",
                ats.raw_data.get(
                    "designation"
                )
                if ats else None
            )
        ]

        for source, value in candidates:

            evidence = self._create_evidence(
                source,
                value
            )

            if evidence:
                evidences.append(
                    evidence
                )

        return evidences

    def build(
        self,
        parsed_sources: Dict
    ) -> CanonicalCandidate:

        resolved_name = (
            self.field_resolver.resolve(
                self._collect_name_evidence(
                    parsed_sources
                )
            )
        )

        resolved_email = (
            self.field_resolver.resolve(
                self._collect_email_evidence(
                    parsed_sources
                )
            )
        )

        resolved_phone = (
            self.field_resolver.resolve(
                self._collect_phone_evidence(
                    parsed_sources
                )
            )
        )

        resolved_company = (
            self.field_resolver.resolve(
                self._collect_company_evidence(
                    parsed_sources
                )
            )
        )

        resolved_title = (
            self.field_resolver.resolve(
                self._collect_title_evidence(
                    parsed_sources
                )
            )
        )

        aggregated_skills = (
            self.skill_aggregator.aggregate(
                parsed_sources
            )
        )

        return CanonicalCandidate(
            candidate_id=
            f"cand_{uuid4().hex[:8]}",

            full_name=resolved_name,

            primary_email=resolved_email,

            primary_phone=resolved_phone,

            current_company=resolved_company,

            current_title=resolved_title,

            skills=aggregated_skills
        )
