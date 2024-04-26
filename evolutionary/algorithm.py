from typing import Callable, Sequence
import random


class Individual:
    def __init__(
            self,
            genome: list,
            fitness_fn: Callable[[list], float],
            mutation_fn: Callable[[list], list],
            crossover_fn: Callable[[list, list], Sequence[list]]
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
        return self.fitness_fn(self.genome)

    def mutate(self) -> 'Individual':
        self.genome = self.mutation_fn(self.genome)

    def crossover(self, other: 'Individual') -> Sequence['Individual']:
        offspring_genomes = self.crossover_fn(self.genome, other.genome)
        offspring = [
            Individual(offspring_genomes[i], self.fitness_fn, self.mutation_fn, self.crossover_fn)
            for i in range(len(offspring_genomes))
        ]
        return offspring


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
            print('Generation [{:<2}/{:<2}] - Average fitness = {:<4.2f}'.format(
                generation + 1,
                max_generations,
                self.population.fitness())
            )

            next_generation = []
            pool = self.population.mating_pool(len(self.population))

            for _ in range(len(self.population) // 2):
                parent1, parent2 = random.choices(pool, k=2)
                offspring = parent1.crossover(parent2)
                for child in offspring:
                    child.mutate()
                next_generation += offspring
            self.population = Population(next_generation, self.population.selection_fn)

    def fittest(self) -> Individual:
        return max(self.population.individuals, key=lambda individual: individual.fitness())
