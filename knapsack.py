from evolutionary.algorithm import Individual, Population
from evolutionary.mutation import RandomBitFlip
from evolutionary.crossover import SinglePoint
from evolutionary.selection import TournamentSelection
from evolutionary.algorithm import Evolution
import numpy as np

N_ITEMS = 8
MAX_WEIGHT = 20
POPULATION_SIZE = 10
MAX_GENERATIONS = 20
SELECTION_FN = TournamentSelection(7, 1)
MUTATION_FN = RandomBitFlip(.01)
CROSSOVER_FN = SinglePoint()


weights = np.random.randint(1, 10, size=N_ITEMS)
values = np.random.randint(1, 10, size=N_ITEMS)
fitness_fn = lambda genome: (np.array(genome) * values).sum() if (np.array(genome) * weights).sum() <= MAX_WEIGHT else 0

population = Population([
    Individual(
        np.random.choice([0, 1], N_ITEMS).tolist(),
        fitness_fn,
        MUTATION_FN,
        CROSSOVER_FN
    ) for _ in range(POPULATION_SIZE)
], SELECTION_FN)

evolution = Evolution(population)
evolution.simulate(MAX_GENERATIONS)
print('Fittest individual -', evolution.fittest())
