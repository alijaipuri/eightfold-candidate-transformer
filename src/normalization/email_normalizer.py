import re
from typing import Optional

from src.normalization.base import BaseNormalizer


class EmailNormalizer(BaseNormalizer):
    """
    Normalizes email addresses into canonical lowercase format.
    """

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def normalize(
        self,
        value: Optional[str]
    ) -> Optional[str]:

        if not value:
            return None

        email = value.strip().lower()

        if not self.EMAIL_PATTERN.match(email):
            return None

        return email
