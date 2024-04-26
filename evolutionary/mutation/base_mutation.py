from abc import ABC, abstractmethod


class BaseMutation(ABC):
    @abstractmethod
    def __call__(self, genome: list) -> list: ...
