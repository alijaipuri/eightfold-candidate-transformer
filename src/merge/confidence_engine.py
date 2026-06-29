from dataclasses import dataclass
from typing import List


@dataclass
class FieldEvidence:
    source: str
    value: str
    confidence: float


class ConfidenceEngine:

    AGREEMENT_BONUS = 0.05
    MAX_CONFIDENCE = 1.0

    @classmethod
    def calculate(
        cls,
        evidences: List[FieldEvidence]
    ) -> float:

        if not evidences:
            return 0.0

        base_confidence = max(
            evidence.confidence
            for evidence in evidences
        )

        unique_values = {
            evidence.value.lower()
            for evidence in evidences
        }

        agreement_bonus = (
            len(evidences) - len(unique_values)
        ) * cls.AGREEMENT_BONUS

        return min(
            base_confidence + agreement_bonus,
            cls.MAX_CONFIDENCE
        )
