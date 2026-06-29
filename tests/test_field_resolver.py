from src.merge.field_evidence import (
    FieldEvidence
)

from src.merge.field_resolver import (
    FieldResolver
)


def test_highest_confidence_source_selected():

    resolver = FieldResolver()

    evidences = [
        FieldEvidence(
            source="resume",
            value="OpenAI",
            source_confidence=0.80
        ),
        FieldEvidence(
            source="recruiter_csv",
            value="OpenAI",
            source_confidence=0.95
        ),
    ]

    result = resolver.resolve(
        evidences
    )

    assert result.value == "OpenAI"

    assert (
        result.selected_source
        == "recruiter_csv"
    )


def test_alternative_values_preserved():

    resolver = FieldResolver()

    evidences = [
        FieldEvidence(
            source="resume",
            value="Google",
            source_confidence=0.80
        ),
        FieldEvidence(
            source="recruiter_csv",
            value="OpenAI",
            source_confidence=0.95
        ),
    ]

    result = resolver.resolve(
        evidences
    )

    assert "Google" in result.alternatives
