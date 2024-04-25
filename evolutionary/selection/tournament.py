import evolutionary.algorithm as alg
from evolutionary.selection.base_selection import BaseSelection
from typing import Sequence
import random


class TournamentSelection(BaseSelection):
    def __init__(self, n_participants: int, p: float):
        self.n_participants = n_participants
        self.p = p

    def __call__(self, population: 'alg.Population', size: int) -> Sequence['alg.Individual']:
        pool = []
        for _ in range(size):
            participants = random.choices(population.individuals, k=self.n_participants)
            if random.random() < self.p:
                pool.append(max(participants, key=lambda participant: participant.fitness()))
            else:
                pool.append(random.choice(participants))
        return pool
