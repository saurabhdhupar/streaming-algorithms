from datetime import datetime
import random

from approx_counting.morris_algorithm import MorrisAlgorithm


class MorrisPlusAlgorithm(MorrisAlgorithm):

    def __init__(self, total_estimators: int, seed: int = datetime.now()) -> None:
        self.estimators = [MorrisAlgorithm(seed)]*total_estimators

    def increment(self) -> None:
        idx = random.randint(0, len(self.estimators) - 1)
        self.estimators[idx].increment()

    def approx_count(self) -> int:
        total_sum = sum([estimator.approx_count() for estimator in self.estimators])
        return total_sum/len(self.estimators)
