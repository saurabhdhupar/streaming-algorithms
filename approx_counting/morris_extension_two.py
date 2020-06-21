import random
from datetime import datetime
import math
from approx_counting.morris_algorithm import MorrisAlgorithm
from approx_counting.morris_extension_one import MorrisPlusAlgorithm
from statistics import median


class MorrisPlusPlusAlgorithm(MorrisAlgorithm):

    def __init__(self, total_estimators: int, total_weak_estimators: int,
                 seed: int = datetime.now().microsecond) -> None:
        self.total_weak_estimators = total_weak_estimators
        self.estimators = []
        self.random = random.Random(seed)
        multiplier = pow(10, math.log(seed, 10))
        for i in range(total_weak_estimators):
            new_seed = self.random.uniform(-total_weak_estimators, total_weak_estimators) * multiplier
            self.estimators.append(MorrisPlusAlgorithm(total_estimators, new_seed))

    def increment(self) -> None:
        for idx in range(self.total_weak_estimators):
            self.estimators[idx].increment()

    def approx_count(self) -> int:
        approx_counts = [estimator.approx_count() for estimator in self.estimators]
        return median(approx_counts)
