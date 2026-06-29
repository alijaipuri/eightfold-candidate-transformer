from src.matching.match_result import (
    MatchEvidence,
    MatchResult
)
from src.matching.scoring_engine import (
    MatchingScoringEngine
)


class CandidateMatcher:

    def __init__(self):
        self.engine = MatchingScoringEngine()

    def match(
        self,
        candidate_a: dict,
        candidate_b: dict
    ) -> MatchResult:

        email_score = self.engine.email_score(
            candidate_a.get("email"),
            candidate_b.get("email")
        )

        phone_score = self.engine.phone_score(
            candidate_a.get("phone"),
            candidate_b.get("phone")
        )

        name_score = self.engine.name_score(
            candidate_a.get("name"),
            candidate_b.get("name")
        )

        final_score = (
            email_score
            * self.engine.EMAIL_WEIGHT
            +
            phone_score
            * self.engine.PHONE_WEIGHT
            +
            name_score
            * self.engine.NAME_WEIGHT
        )

        evidences = []

        evidences.append(
            MatchEvidence(
                attribute="email",
                source_a="candidate_a",
                source_b="candidate_b",
                value_a=str(
                    candidate_a.get("email")
                ),
                value_b=str(
                    candidate_b.get("email")
                ),
                similarity_score=email_score
            )
        )

        evidences.append(
            MatchEvidence(
                attribute="phone",
                source_a="candidate_a",
                source_b="candidate_b",
                value_a=str(
                    candidate_a.get("phone")
                ),
                value_b=str(
                    candidate_b.get("phone")
                ),
                similarity_score=phone_score
            )
        )

        evidences.append(
            MatchEvidence(
                attribute="name",
                source_a="candidate_a",
                source_b="candidate_b",
                value_a=str(
                    candidate_a.get("name")
                ),
                value_b=str(
                    candidate_b.get("name")
                ),
                similarity_score=name_score
            )
        )

        confidence_level = (
            "HIGH"
            if final_score >= 0.90
            else (
                "MEDIUM"
                if final_score >= 0.75
                else "LOW"
            )
        )

        return MatchResult(
            candidate_match=(
                final_score >=
                self.engine.MATCH_THRESHOLD
            ),
            overall_score=final_score,
            confidence_level=confidence_level,
            evidences=evidences,
            weighted_breakdown={
                "email": email_score,
                "phone": phone_score,
                "name": name_score
            }
        )
