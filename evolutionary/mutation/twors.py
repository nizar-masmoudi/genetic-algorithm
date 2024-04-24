import random
from evolutionary.mutation.base_mutation import BaseMutation
import evolutionary.algorithm as alg


class TWORS(BaseMutation):
    def __init__(self, rate: float):
        super().__init__()
        self.rate = rate

    def __call__(self, individual: 'alg.Individual') -> 'alg.Individual':
        if random.random() < self.rate:
            i, j = random.randint(0, len(individual) - 1), random.randint(0, len(individual) - 1)
            individual.genome[i], individual.genome[j] = individual.genome[j], individual.genome[i]
        return individual
