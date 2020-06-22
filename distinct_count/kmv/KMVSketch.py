import random
from datetime import datetime
from distinct_count.distinct_count import DistinctCounterEstimator


class KMVSketch(DistinctCounterEstimator):

    def __init__(self, seed: float = datetime.now().timestamp()) -> None:
        self.random = random.Random(seed)
        self.min_hash = 1.0

    def increment(self, element: object):
        r = self.random.uniform(0, 1)
        if r < self.min_hash:
            self.min_hash = r

    def approx_distinct_count(self) -> float:
        return (1.0/self.min_hash) - 1



