from src.normalization.phone_normalizer import (
    PhoneNormalizer
)


def test_indian_phone_normalization():
    normalizer = PhoneNormalizer()

    result = normalizer.normalize(
        "9876543210"
    )

    assert result == "+919876543210"


def test_e164_phone_preserved():
    normalizer = PhoneNormalizer()

    result = normalizer.normalize(
        "+919876543210"
    )

    assert result == "+919876543210"


def test_invalid_phone_returns_none():
    normalizer = PhoneNormalizer()

    result = normalizer.normalize(
        "123"
    )

    assert result is None
