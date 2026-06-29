from typing import Optional

import pycountry

from src.normalization.base import BaseNormalizer


class LocationNormalizer(BaseNormalizer):

    def normalize(
        self,
        value: Optional[str]
    ) -> Optional[str]:

        if not value:
            return None

        value = value.strip()

        countries = {
            country.name.lower(): country.name
            for country in pycountry.countries
        }

        return countries.get(
            value.lower(),
            value
        )
