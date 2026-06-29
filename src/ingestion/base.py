from abc import ABC, abstractmethod

from src.models.source import SourcePayload


class BaseSourceParser(ABC):
    """
    Common interface for all candidate data source parsers.
    """

    source_name: str

    @abstractmethod
    def parse(
        self,
        file_path: str
    ) -> SourcePayload:
        """
        Parse raw source data into a standardized payload.
        """
        pass
