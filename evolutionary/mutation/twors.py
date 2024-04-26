import random
from evolutionary.mutation.base_mutation import BaseMutation
import evolutionary.algorithm as alg


class TWORS(BaseMutation):
    def __init__(self, rate: float):
        super().__init__()
        self.rate = rate

    def __call__(self, genome: list) -> list:
        if random.random() < self.rate:
            i, j = random.randint(0, len(genome) - 1), random.randint(0, len(genome) - 1)
            genome[i], genome[j] = genome[j], genome[i]
        return genome
