from src.projection.base import BaseProjector


class CandidateProjector(
    BaseProjector
):

    def project(
        self,
        canonical_candidate,
        config
    ):

        projected = {}

        candidate_dict = (
            canonical_candidate.model_dump()
        )

        for field in config.fields:

            if field in candidate_dict:
                projected[field] = (
                    candidate_dict[field]
                )

        return projected
