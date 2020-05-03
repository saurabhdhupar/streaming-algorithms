import random
from datetime import datetime

from approx_counting.morris_algorithm import MorrisAlgorithm
from approx_counting.morris_extension_one import MorrisPlusAlgorithm


class MorrisPlusPlusAlgorithm(MorrisAlgorithm):

    def __init__(self, total_estimators: int, total_weak_estimators: int, seed: int = datetime.now()) -> None:
        self.estimators = [MorrisPlusAlgorithm(total_estimators, seed)] * total_weak_estimators

    def increment(self) -> None:
        idx = random.randint(0, len(self.estimators) - 1)
        self.estimators[idx].increment()

    def approx_count(self) -> int:
        size = len(self.estimators)
        approx_counts = sorted([estimator.approx_count() for estimator in self.estimators])
        return (sum(approx_counts[size // 2 - 1:size // 2 + 1]) / 2.0, approx_counts[size // 2])[size % 2]
