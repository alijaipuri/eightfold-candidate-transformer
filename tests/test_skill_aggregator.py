from src.merge.skill_aggregator import (
    SkillAggregator
)


class MockSource:
    def __init__(self, data):
        self.raw_data = data


def test_skill_aggregation():

    aggregator = SkillAggregator()

    parsed_sources = {
        "github_profile": MockSource(
            {
                "languages": [
                    "Python",
                    "Docker"
                ]
            }
        ),
        "linkedin_profile": MockSource(
            {
                "skills": [
                    "Python",
                    "FastAPI"
                ]
            }
        ),
        "ats_json": MockSource(
            {
                "skills": [
                    "Python"
                ]
            }
        )
    }

    result = aggregator.aggregate(
        parsed_sources
    )

    names = [
        skill.skill_name
        for skill in result
    ]

    assert "Python" in names

    python_skill = next(
        skill
        for skill in result
        if skill.skill_name == "Python"
    )

    assert (
        python_skill.occurrence_count
        == 3
    )
