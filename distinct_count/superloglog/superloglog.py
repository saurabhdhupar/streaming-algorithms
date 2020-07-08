import math
import random

from distinct_count.loglog.loglog import LogLogEstimator


class SuperLogLogEstimator(LogLogEstimator):

    def __init__(self,
                 num_buckets: int,
                 seed: int = random.randint(-214783648, 2147483647)) -> None:
        super().__init__(num_buckets=num_buckets, seed=seed)
        self.max_value = 10 ** 19
        self.threshold_max_bucket_value = math.ceil(math.log(self.max_value / self.num_buckets, 2) + 3)

    def approx_distinct_count(self) -> float:
        sorted(self.max_hash_value_by_buckets)
        alpha = 1.09295
        cutoff_idx = math.floor(0.7 * self.num_buckets)
        total_sum = 0
        for x in self.max_hash_value_by_buckets[:cutoff_idx]:
            if 0 < x < self.threshold_max_bucket_value:
                total_sum += x

        mean_value = total_sum / float(cutoff_idx)
        return alpha * cutoff_idx * (2 ** (mean_value - 1))
