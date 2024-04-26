from evolutionary.crossover.base_crossover import BaseCrossover
import evolutionary.algorithm as alg
from typing import Sequence
import random


class SinglePoint(BaseCrossover):
    def __call__(self, parent1: list, parent2: list) -> Sequence[list]:
        point = random.randint(0, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
