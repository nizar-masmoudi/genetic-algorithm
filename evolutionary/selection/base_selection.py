from abc import ABC, abstractmethod
import evolutionary.algorithm as alg
from typing import Sequence


class BaseSelection(ABC):
    @abstractmethod
    def __call__(self, population: 'alg.Population', size: int) -> Sequence['alg.Individual']: ...
