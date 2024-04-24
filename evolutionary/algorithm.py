from typing import Callable, Sequence, List


class Individual:
    def __init__(
            self,
            genome: list,
            fitness_fn: Callable[[list], float],
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
        return '|' + '|'.join(['{:^3}'.format(gene) for gene in self.genome]) + '|'

    def fitness(self) -> float:
        return self.fitness_fn(self.genome)

    def mutate(self) -> 'Individual':
        return self.mutation_fn(self)

    def crossover(self, other: 'Individual') -> Sequence['Individual']:
        return self.crossover_fn(self, other)


class Population:
    def __init__(self, individuals: List[Individual]):
        self.individuals = individuals

    def fitness(self) -> float:
        pass

    def mating_pool(self, size: int) -> List['Individual']:
        return self.individuals


class Evolution:
    def __init__(self):
        pass

    def simulate(self):
        pass
