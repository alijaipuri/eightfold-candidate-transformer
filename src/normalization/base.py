from abc import ABC, abstractmethod
from typing import Any


class BaseNormalizer(ABC):
    """
    Base interface for all normalization components.
    """

    @abstractmethod
    def normalize(self, value: Any):
        pass
