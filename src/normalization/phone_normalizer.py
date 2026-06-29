from typing import Optional

import phonenumbers

from src.normalization.base import BaseNormalizer


class PhoneNormalizer(BaseNormalizer):
    """
    Converts phone numbers into E.164 format.
    """

    def normalize(
        self,
        value: Optional[str]
    ) -> Optional[str]:

        if not value:
            return None

        try:
            parsed = phonenumbers.parse(
                value,
                "IN"
            )

            if not phonenumbers.is_valid_number(parsed):
                return None

            return phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.E164
            )

        except Exception:
            return None
