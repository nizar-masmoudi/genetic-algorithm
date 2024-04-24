from abc import ABC, abstractmethod
import evolutionary.algorithm as alg
from typing import Tuple


class BaseCrossover(ABC):
    @abstractmethod
    def __call__(self, parent1: alg.Individual, parent2: alg.Individual) -> Tuple['alg.Individual']: ...
