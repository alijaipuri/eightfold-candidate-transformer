class SourceParsingError(Exception):
    """
    Raised when a source parser fails to process input data.
    """

    pass


class SourceValidationError(Exception):
    """
    Raised when input source data violates schema rules.
    """

    pass
