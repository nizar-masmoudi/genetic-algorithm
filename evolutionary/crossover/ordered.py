from evolutionary.crossover.base_crossover import BaseCrossover
from typing import Sequence
import random


class OX(BaseCrossover):
    def __call__(self, parent1: list, parent2: list) -> Sequence[list]:
        parents = (parent1, parent2)
        offspring = [[None for _1 in range(len(parent1))] for _2 in range(2)]
        for i in range(2):
            start = random.randint(0, len(parent1) - 2)
            end = random.randint(start + 1, len(parent1) - 1)
            sample = parents[i][start:end]
            offspring[i][start:end] = sample
            rest = [gene for gene in parents[1 - i] if gene not in sample]
            offspring[i][:start] = rest[:start]
            offspring[i][end:] = rest[start:]
        return offspring
