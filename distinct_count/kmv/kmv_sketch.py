import random
import sys

import mmh3

from distinct_count.distinct_count import DistinctCounterEstimator


class KMVSketch(DistinctCounterEstimator):

    def __init__(self, seed: int = random.randint(-214783648, 2147483647)) -> None:
        self.min_hash = 1.0
        self.seed = seed
        self.max_size = 2**32

    def increment(self, element: object):
        element_str = str(element).encode('utf-8')
        h = mmh3.hash(element_str, seed=self.seed, signed=False) / self.max_size
        if h < self.min_hash:
            self.min_hash = h

    def approx_distinct_count(self) -> float:
        return (1.0/self.min_hash) - 1
