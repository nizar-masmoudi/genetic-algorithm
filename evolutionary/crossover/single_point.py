from evolutionary.crossover.base_crossover import BaseCrossover
import evolutionary.algorithm as alg
from typing import Sequence
import random


class SinglePoint(BaseCrossover):
    def __call__(self, parent1: alg.Individual, parent2: alg.Individual) -> Sequence['alg.Individual']:
        point = random.randint(0, len(parent1) - 1)
        child1 = alg.Individual(
            genome=parent1.genome[:point] + parent2.genome[point:],
            fitness_fn=parent1.fitness_fn,
            mutation_fn=parent1.mutation_fn,
            crossover_fn=parent1.crossover_fn
        )
        child2 = alg.Individual(
            genome=parent2.genome[:point] + parent1.genome[point:],
            fitness_fn=parent1.fitness_fn,
            mutation_fn=parent1.mutation_fn,
            crossover_fn=parent1.crossover_fn
        )
        return child1, child2
