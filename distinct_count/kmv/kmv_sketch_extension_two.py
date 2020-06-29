import random
import sys
from statistics import median

from distinct_count.kmv.kmv_sketch_extension_one import KMVSketchMeanEstimator


class KMVSketchMedianOfMeanEstimator(KMVSketchMeanEstimator):

    def __init__(self, total_estimators: int,
                 total_weak_estimators: int,
                 seed: int = random.randint(-214783648, 2147483647)) -> None:
        self.total_estimators = total_estimators
        self.estimators = []
        self.random = random.Random(seed)
        for i in range(total_estimators):
            new_seed = self.random.randint(-sys.maxsize - 1, sys.maxsize - 1)
            self.estimators.append(KMVSketchMeanEstimator(total_estimators=total_weak_estimators,
                                                          seed=new_seed))

    def approx_distinct_count(self) -> int:
        distinct_counts = [estimator.approx_distinct_count() for estimator in self.estimators]
        return median(distinct_counts)