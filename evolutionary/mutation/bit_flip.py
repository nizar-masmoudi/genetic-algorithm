import random
from evolutionary.mutation.base_mutation import BaseMutation
import evolutionary.algorithm as alg


class RandomBitFlip(BaseMutation):
    def __init__(self, rate: float):
        super().__init__()
        self.rate = rate

    def __call__(self, genome: list) -> list:
        for i, gene in enumerate(genome):
            if gene not in [0, 1]:
                raise ValueError('RandomBitFlip requires a bit string genome.')
            else:
                if random.random() < self.rate:
                    genome[i] = 1 - gene
        return genome
