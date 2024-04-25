import evolutionary.algorithm as alg
from evolutionary.selection.base_selection import BaseSelection
from typing import Sequence
import random


class RandomSelection(BaseSelection):
    def __call__(self, population: 'alg.Population', size: int) -> Sequence['alg.Individual']:
        return random.choices(population.individuals, k=size)
