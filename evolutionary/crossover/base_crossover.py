from abc import ABC, abstractmethod
from typing import Sequence


class BaseCrossover(ABC):
    @abstractmethod
    def __call__(self, parent1: list, parent2: list) -> Sequence[list]: ...
