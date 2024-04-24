from evolutionary.algorithm import Individual
from evolutionary.crossover import OX, SinglePoint
import random


class TestCrossover:
    def test_single_point(self):
        random.seed(156)
        parent1 = Individual(['a', 'b', 'c', 'd', 'e'], None, None, SinglePoint())
        parent2 = Individual(['a', 'd', 'e', 'c', 'b'], None, None, SinglePoint())
        child1, child2 = parent1.crossover(parent2)
        assert child1 == Individual(['a', 'b', 'c', 'c', 'b'], None, None, None)
        assert child2 == Individual(['a', 'd', 'e', 'd', 'e'], None, None, None)

    def test_ox(self):
        random.seed(156)
        parent1 = Individual(['a', 'b', 'c', 'd', 'e'], None, None, OX())
        parent2 = Individual(['a', 'd', 'e', 'c', 'b'], None, None, OX())
        child1, child2 = parent1.crossover(parent2)
        assert child1 == Individual(['a', 'e', 'c', 'd', 'b'], None, None, None)
        assert child2 == Individual(['a', 'd', 'e', 'b', 'c'], None, None, None)
