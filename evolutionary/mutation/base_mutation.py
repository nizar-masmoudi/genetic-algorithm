from abc import ABC, abstractmethod
import evolutionary.algorithm as alg


class BaseMutation(ABC):
    @abstractmethod
    def __call__(self, individual: 'alg.Individual') -> 'alg.Individual': ...
