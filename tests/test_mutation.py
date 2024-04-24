from evolutionary.mutation import RandomBitFlip, TWORS
from evolutionary.algorithm import Individual
import random


class TestMutation:
    def test_bitflip(self):
        random.seed(123)
        mutation_fn = RandomBitFlip(.5)
        individual1 = Individual([0, 1, 0, 1, 0], None, mutation_fn, None)
        individual1 = individual1.mutate()
        assert individual1 == Individual([1, 0, 1, 0, 0], None, None, None)

    def test_twors(self):
        random.seed(123)
        mutation_fn = TWORS(.5)
        individual1 = Individual(['a', 'b', 'c', 'd', 'e'], None, mutation_fn, None)
        individual1 = individual1.mutate()
        assert individual1 == Individual(['d', 'b', 'c', 'a', 'e'], None, None, None)