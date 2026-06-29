class ProvenanceGenerator:

    @staticmethod
    def generate(
        canonical_candidate
    ) -> dict:

        provenance = {}

        fields = [
            "full_name",
            "primary_email",
            "primary_phone",
            "current_company",
            "current_title"
        ]

        for field in fields:

            value = getattr(
                canonical_candidate,
                field
            )

            provenance[field] = {
                "selected_source":
                value.selected_source,

                "supporting_sources":
                value.supporting_sources,

                "alternatives":
                value.alternatives,

                "confidence":
                value.confidence,

                "resolution_strategy":
                "highest_source_confidence"
            }

        return provenance
