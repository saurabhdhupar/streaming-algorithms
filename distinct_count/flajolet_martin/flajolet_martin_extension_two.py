import random
from datetime import datetime
from statistics import median

from distinct_count.flajolet_martin.flajolet_martin_extension_one import FlajoletMartinMeanEstimator


class FlajoletMartinMedianOfMeanEstimator(FlajoletMartinMeanEstimator):

    def __init__(self, sketch_size: int,
                 total_estimators: int,
                 total_weak_estimators: int,
                 seed: float = datetime.now().timestamp(),
                 hashing_function: str = 'murmurhash3') -> None:
        self.total_estimators = total_estimators
        self.estimators = []
        self.random = random.Random(seed)
        for i in range(total_estimators):
            new_seed = self.random.uniform(-total_estimators, total_estimators)
            self.estimators.append(FlajoletMartinMeanEstimator(sketch_size=sketch_size,
                                                               total_estimators=total_weak_estimators,
                                                               hashing_function=hashing_function,
                                                               seed=new_seed))

    def approx_distinct_count(self) -> int:
        distinct_counts = [estimator.approx_distinct_count() for estimator in self.estimators]
        return median(distinct_counts)
