from evolutionary.crossover.base_crossover import BaseCrossover
import evolutionary.algorithm as alg
from typing import Sequence
import random


class OX(BaseCrossover):
    def __call__(self, parent1: alg.Individual, parent2: alg.Individual) -> Sequence['alg.Individual']:
        parents = (parent1, parent2)
        offspring = [
            alg.Individual(
                genome=[None for _ in range(len(parent1))],
                fitness_fn=parent1.fitness_fn,
                mutation_fn=parent1.mutation_fn,
                crossover_fn=parent1.crossover_fn
            ),
            alg.Individual(
                genome=[None for _ in range(len(parent1))],
                fitness_fn=parent1.fitness_fn,
                mutation_fn=parent1.mutation_fn,
                crossover_fn=parent1.crossover_fn
            ),
        ]
        for i in range(2):
            start = random.randint(0, len(parent1) - 2)
            end = random.randint(start + 1, len(parent1) - 1)
            sample = parents[i].genome[start:end]
            offspring[i].genome[start:end] = sample
            rest = [gene for gene in parents[1 - i].genome if gene not in sample]
            offspring[i].genome[:start] = rest[:start]
            offspring[i].genome[end:] = rest[start:]
        return offspring
