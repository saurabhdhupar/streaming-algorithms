from datetime import datetime
import random

from approx_counting.morris_algorithm import MorrisAlgorithm


class MorrisPlusAlgorithm(MorrisAlgorithm):

    def __init__(self, total_estimators: int, seed: float = datetime.now().timestamp()) -> None:
        self.total_estimators = total_estimators
        self.estimators = []
        self.random = random.Random(seed)
        for i in range(total_estimators):
            new_seed = self.random.uniform(-total_estimators, total_estimators)
            self.estimators.append(MorrisAlgorithm(new_seed))

    def increment(self) -> None:
        for idx in range(self.total_estimators):
            self.estimators[idx].increment()

    def approx_count(self) -> int:
        total_sum = sum([estimator.counter for estimator in self.estimators])
        mean_val = total_sum / self.total_estimators
        return 2 ** mean_val - 1
