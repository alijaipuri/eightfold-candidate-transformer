from abc import ABC, abstractmethod


class BaseProjector(ABC):

    @abstractmethod
    def project(
        self,
        canonical_candidate,
        config
    ):
        pass
