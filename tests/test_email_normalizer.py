from src.normalization.email_normalizer import EmailNormalizer


def test_email_normalization_lowercase():
    normalizer = EmailNormalizer()

    result = normalizer.normalize(
        "ALI@EXAMPLE.COM"
    )

    assert result == "ali@example.com"


def test_email_normalization_whitespace():
    normalizer = EmailNormalizer()

    result = normalizer.normalize(
        "  ali@example.com  "
    )

    assert result == "ali@example.com"


def test_invalid_email_returns_none():
    normalizer = EmailNormalizer()

    result = normalizer.normalize(
        "not-an-email"
    )

    assert result is None
