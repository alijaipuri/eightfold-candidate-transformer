import re
from typing import Optional

from src.normalization.base import BaseNormalizer


class NameNormalizer(BaseNormalizer):
    """
    Standardizes candidate names.
    """

    def normalize(
        self,
        value: Optional[str]
    ) -> Optional[str]:

        if not value:
            return None

        value = value.strip()

        value = re.sub(
            r"\s+",
            " ",
            value
        )

        return value.title()
