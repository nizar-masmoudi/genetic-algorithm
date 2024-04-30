from evolutionary.algorithm import Individual, Population
from evolutionary.mutation import RandomBitFlip
from evolutionary.crossover import SinglePoint
from evolutionary.selection import TournamentSelection
import random
from evolutionary.algorithm import Evolution
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

N_ITEMS = 8
MAX_WEIGHT = 20

weights = np.random.randint(1, 10, size=N_ITEMS)
values = np.random.randint(1, 10, size=N_ITEMS)


fitness_fn = lambda genome: (np.array(genome) * values).sum() if (np.array(genome) * weights).sum() <= MAX_WEIGHT else 0
selection_fn = TournamentSelection(7, 1)
mutation_fn = RandomBitFlip(.01)
crossover_fn = SinglePoint()


population = Population([
    Individual(np.random.choice([0, 1], N_ITEMS).tolist(), fitness_fn, mutation_fn, crossover_fn) for _ in range(10)
], selection_fn)

evolution = Evolution(population)
evolution.simulate(20)

print(''.join(['{:<3}'.format(w) for w in weights]))
print(''.join(['{:<3}'.format(v) for v in values]))
print('-'*50)
print()
for individual in evolution.population.individuals:
    print(individual, '->', round(individual.fitness(), 3))
