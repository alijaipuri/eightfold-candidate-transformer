from rapidfuzz import fuzz


class MatchingScoringEngine:

    EMAIL_WEIGHT = 0.45
    PHONE_WEIGHT = 0.35
    NAME_WEIGHT = 0.20

    MATCH_THRESHOLD = 0.75

    @staticmethod
    def email_score(
        email_a: str | None,
        email_b: str | None
    ) -> float:

        if not email_a or not email_b:
            return 0.0

        return 1.0 if email_a == email_b else 0.0

    @staticmethod
    def phone_score(
        phone_a: str | None,
        phone_b: str | None
    ) -> float:

        if not phone_a or not phone_b:
            return 0.0

        return 1.0 if phone_a == phone_b else 0.0

    @staticmethod
    def name_score(
        name_a: str | None,
        name_b: str | None
    ) -> float:

        if not name_a or not name_b:
            return 0.0

        return (
            fuzz.token_sort_ratio(
                name_a,
                name_b
            ) / 100
        )
