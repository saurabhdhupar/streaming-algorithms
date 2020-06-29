import random
import sys
from datetime import datetime
from distinct_count.distinct_count import DistinctCounterEstimator
from distinct_count.kmv.kmv_sketch import KMVSketch


class KMVSketchMeanEstimator(DistinctCounterEstimator):

    def __init__(self, total_estimators: int, seed: int = random.randint(-214783648, 2147483647)) -> None:
        self.random = random.Random(seed)
        self.min_hash = 1.0
        self.total_estimators = total_estimators
        self.estimators = []
        for i in range(total_estimators):
            new_seed = self.random.randint(-sys.maxsize - 1, sys.maxsize - 1)
            self.estimators.append(KMVSketch(new_seed))

    def increment(self, element: object):
        for idx in range(self.total_estimators):
            self.estimators[idx].increment(element)

    def approx_distinct_count(self) -> float:
        total_sum = sum([estimator.min_hash for estimator in self.estimators])
        mean_val = total_sum / self.total_estimators
        return (1.0/mean_val) - 1
