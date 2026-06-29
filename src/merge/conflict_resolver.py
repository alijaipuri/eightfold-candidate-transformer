from typing import Dict, List, Tuple

from src.merge.source_weights import (
    SOURCE_CONFIDENCE_WEIGHTS
)


class ConflictResolver:

    @staticmethod
    def resolve(
        field_name: str,
        candidates: List[Tuple[str, str]]
    ) -> Dict:

        if not candidates:
            return {
                "value": None,
                "confidence": 0.0,
                "source": None,
            }

        ranked = sorted(
            candidates,
            key=lambda x:
            SOURCE_CONFIDENCE_WEIGHTS.get(
                x[0],
                0.0
            ),
            reverse=True
        )

        selected_source, selected_value = ranked[0]

        return {
            "field": field_name,
            "value": selected_value,
            "source": selected_source,
            "confidence":
            SOURCE_CONFIDENCE_WEIGHTS[
                selected_source
            ],
            "alternatives": ranked[1:]
        }
