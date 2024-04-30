from evolutionary.algorithm import Individual, Population
from evolutionary.mutation import TWORS
from evolutionary.crossover import OX
from evolutionary.selection import TournamentSelection
import random
from evolutionary.algorithm import Evolution
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

N_NODES = 20
nodes = list(range(N_NODES))
coordinates = np.random.randint(0, 10, size=(N_NODES, 2))

dist_matrix = np.sqrt(((coordinates[:, None] - coordinates) ** 2).sum(axis=-1))


def fitness_fn(genome: list) -> float:
    return 1 / dist_matrix[genome, genome[-1:] + genome[0:-1]].sum()


individuals = []
node_indices = list(range(len(coordinates)))
for _ in range(10):
    rand_genome = random.sample(nodes, len(nodes))
    individuals.append(Individual(rand_genome, fitness_fn, TWORS(.1), OX()))
population = Population(individuals, TournamentSelection(5, .7))

for individual in population.individuals:
    print(individual, '->', round(1/individual.fitness(), 3))


evolution = Evolution(population)
evolution.simulate(10)
print()
for individual in evolution.population.individuals:
    print(individual, '->', round(1/individual.fitness(), 3))

fittest = evolution.fittest()

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from([(fittest.genome[i-1], fittest.genome[i]) for i in range(len(fittest))])
pos = {nodes[i]: coordinates[i] for i in range(len(coordinates))}

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos, font_color='w')
nx.draw_networkx_edges(G, pos)
plt.show()
