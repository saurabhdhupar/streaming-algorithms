import random
from datetime import datetime
from statistics import median

from distinct_count.distinct_count import DistinctCounterEstimator
from distinct_count.flajolet_martin.flajolet_martin_algorithm import FlajoletMartinAlgorithm


class FlajoletMartinMedianEstimator(DistinctCounterEstimator):

    def __init__(self, sketch_size: int, total_estimators: int,
                 seed: int = random.randint(-214783648, 2147483647),
                 hashing_function: str = 'murmurhash3') -> None:
        self.total_estimators = total_estimators
        self.estimators = []
        self.random = random.Random(seed)
        for i in range(total_estimators):
            new_seed = self.random.randint(-214783648, 2147483647)
            self.estimators.append(FlajoletMartinAlgorithm(sketch_size=sketch_size,
                                                           hashing_function=hashing_function,
                                                           seed=new_seed))

    def increment(self, element: object):
        for idx in range(self.total_estimators):
            self.estimators[idx].increment(element)

    def approx_distinct_count(self) -> int:
        total_sum = [estimator.approx_distinct_count() for estimator in self.estimators]
        return median(total_sum)
