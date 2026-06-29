from src.merge.canonical_builder import (
    CanonicalCandidateBuilder
)


class MockSource:
    def __init__(self, data):
        self.raw_data = data


def test_candidate_builder_generates_profile():

    builder = (
        CanonicalCandidateBuilder()
    )

    parsed_sources = {
        "recruiter_csv": MockSource(
            [
                {
                    "name": "Ali Asgar Jaipuri",
                    "email": "ali@example.com",
                    "phone": "+919876543210",
                    "current_company": "OpenAI",
                    "title": "AI Engineer Intern"
                }
            ]
        ),
        "ats_json": MockSource(
            {
                "candidate_name":
                "Ali A. Jaipuri",

                "primary_email":
                "ali@example.com",

                "phone_number":
                "+919876543210",

                "company":
                "OpenAI",

                "designation":
                "Machine Learning Intern"
            }
        )
    }

    candidate = builder.build(
        parsed_sources
    )

    assert (
        candidate.full_name.value
        == "Ali Asgar Jaipuri"
    )

    assert (
        candidate.current_company.value
        == "OpenAI"
    )
