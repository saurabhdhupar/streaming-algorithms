import random
import sys
from distinct_count.flajolet_martin.flajolet_martin_algorithm import FlajoletMartinAlgorithm


class FlajoletMartinMeanEstimator(FlajoletMartinAlgorithm):

    def __init__(self, sketch_size: int, total_estimators: int,
                 seed: int = random.randint(-214783648, 2147483647),
                 hashing_function: str = 'murmurhash3') -> None:
        self.total_estimators = total_estimators
        self.estimators = []
        self.correction_factor = 0.77351
        self.random = random.Random(seed)
        for i in range(total_estimators):
            new_seed = self.random.randint(-sys.maxsize - 1, sys.maxsize - 1)
            self.estimators.append(FlajoletMartinAlgorithm(sketch_size=sketch_size,
                                                           hashing_function=hashing_function,
                                                           seed=new_seed))

    def increment(self, element: object):
        for idx in range(self.total_estimators):
            self.estimators[idx].increment(element)

    def approx_distinct_count(self) -> int:
        total_sum = sum([estimator.get_max_value() for estimator in self.estimators])
        mean_val = total_sum / self.total_estimators
        return 2**mean_val / self.correction_factor
