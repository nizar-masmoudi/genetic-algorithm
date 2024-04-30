from evolutionary.algorithm import Individual, Population
from evolutionary.mutation import TWORS
from evolutionary.crossover import OX
from evolutionary.selection import TournamentSelection
import random
from evolutionary.algorithm import Evolution
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

N_NODES = 10
POPULATION_SIZE = 20
MAX_GENERATIONS = 20
MUTATION_FN = TWORS(.01)
CROSSOVER_FN = OX()
SELECTION_FN = TournamentSelection(5, .7)

nodes = list(range(N_NODES))
coordinates = np.random.randint(0, 10, size=(N_NODES, 2))

dist_matrix = np.sqrt(((coordinates[:, None] - coordinates) ** 2).sum(axis=-1))


fitness_fn = lambda genome: 1 / dist_matrix[genome, genome[-1:] + genome[0:-1]].sum()

individuals = []
node_indices = list(range(len(coordinates)))
for _ in range(POPULATION_SIZE):
    rand_genome = random.sample(nodes, len(nodes))
    individuals.append(Individual(rand_genome, fitness_fn, MUTATION_FN, CROSSOVER_FN))
population = Population(individuals, SELECTION_FN)

evolution = Evolution(population)
evolution.simulate(MAX_GENERATIONS)
fittest = evolution.fittest()

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from([(fittest.genome[i-1], fittest.genome[i]) for i in range(len(fittest))])
pos = {nodes[i]: coordinates[i] for i in range(len(coordinates))}

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos, font_color='w')
nx.draw_networkx_edges(G, pos)
plt.show()
