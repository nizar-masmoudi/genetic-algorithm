import evolutionary.algorithm as alg
from evolutionary.selection.base_selection import BaseSelection
from typing import Sequence
import random


class LinearRankSelection(BaseSelection):
    def __init__(self, pressure: float):
        self.pressure = max(min(pressure, 2), 1)

    def __call__(self, population: 'alg.Population', size: int) -> Sequence['alg.Individual']:
        individuals = sorted(population.individuals, key=lambda individual: individual.fitness())
        n = len(individuals)
        weights = [
            # https://www.linkedin.com/pulse/selections-genetic-algorithms-ali-karazmoodeh-g9yyf/
            (2 - self.pressure) / n + 2 * (i - 1) * (self.pressure - 1) / (n * (n - 1))
            for i in range(1, n + 1)
        ]
        return random.choices(individuals, weights, k=size)
