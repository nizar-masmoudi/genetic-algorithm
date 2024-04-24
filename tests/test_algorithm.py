from evolutionary.algorithm import Individual


class TestIndividual:
    def test_eq(self):
        individual1 = Individual([0, 1, 0, 1, 0], None, None, None)
        individual2 = Individual([1, 1, 1, 0, 0], None, None, None)
        assert individual1 != individual2
        assert individual1 == individual1
        assert individual2 == individual2

    def test_len(self):
        individual1 = Individual([0, 1, 0, 1, 0], None, None, None)
        assert len(individual1) == 5


# class TestPopulation:
#     def test
