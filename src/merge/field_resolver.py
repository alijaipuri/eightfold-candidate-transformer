from src.merge.field_evidence import (
    FieldEvidence
)

from src.models.canonical import (
    CanonicalField
)


class FieldResolver:

    def resolve(
        self,
        evidences: list[FieldEvidence]
    ) -> CanonicalField:

        if not evidences:
            return CanonicalField(
                value=None,
                confidence=0.0,
                selected_source=None,
                supporting_sources=[],
                alternatives=[]
            )

        evidences = sorted(
            evidences,
            key=lambda x: x.source_confidence,
            reverse=True
        )

        winner = evidences[0]

        supporting_sources = []

        alternatives = []

        for evidence in evidences:
            if evidence.value == winner.value:
                supporting_sources.append(
                    evidence.source
                )
            else:
                alternatives.append(
                    evidence.value
                )

        confidence = min(
            winner.source_confidence
            +
            (0.03 * len(
                supporting_sources
            )),
            1.0
        )

        return CanonicalField(
            value=winner.value,
            confidence=confidence,
            selected_source=winner.source,
            supporting_sources=supporting_sources,
            alternatives=alternatives
        )
