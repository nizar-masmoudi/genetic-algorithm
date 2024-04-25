from typing import Callable, Sequence
import random


class Individual:
    def __init__(
            self,
            genome: list,
            fitness_fn: Callable[['Individual'], float],
            mutation_fn: Callable[['Individual'], 'Individual'],
            crossover_fn: Callable[['Individual', 'Individual'], Sequence['Individual']]
    ):
        self.genome = genome
        self.fitness_fn = fitness_fn
        self.mutation_fn = mutation_fn
        self.crossover_fn = crossover_fn

    def __len__(self) -> int:
        return len(self.genome)

    def __eq__(self, other: 'Individual') -> bool:
        return self.genome == other.genome

    def __repr__(self):
        return ''.join(['{:<3}'.format(gene) for gene in self.genome])

    def fitness(self) -> float:
        return self.fitness_fn(self)

    def mutate(self) -> 'Individual':
        return self.mutation_fn(self)

    def crossover(self, other: 'Individual') -> Sequence['Individual']:
        return self.crossover_fn(self, other)


class Population:
    def __init__(
            self,
            individuals: Sequence[Individual],
            selection_fn: Callable[['Population', int], Sequence[Individual]]
    ):
        self.individuals = individuals
        self.selection_fn = selection_fn

    def __len__(self) -> int:
        return len(self.individuals)

    def __repr__(self):
        return '\n'.join([repr(individual) for individual in self.individuals])

    def fitness(self) -> float:
        # TODO - Add agg_fn as param
        return sum(individual.fitness() for individual in self.individuals) / len(self)

    def mating_pool(self, size: int) -> Sequence['Individual']:
        return self.selection_fn(self, size)


class Evolution:
    def __init__(self, population: Population):
        self.population = population

    def simulate(self, max_generations: int):
        for generation in range(max_generations):
            print('Generation [{:<2}/{:<2}] - Average fitness = {:<4.2f}'.format(generation + 1, max_generations, self.population.fitness()))

            next_generation = []
            pool = self.population.mating_pool(len(self.population))

            for _ in range(len(self.population) // 2):
                parent1, parent2 = random.choices(pool, k=2)
                offspring = parent1.crossover(parent2)
                offspring = [child.mutate() for child in offspring]
                next_generation += offspring
            self.population = Population(next_generation, self.population.selection_fn)

        for individual in self.population.individuals:
            print(individual, '->', individual.fitness())
