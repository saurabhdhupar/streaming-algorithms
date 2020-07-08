import math
import random

import pyhash
import smhasher
import mmh3

from distinct_count.distinct_count import DistinctCounterEstimator

_HASH_FUNCTIONS_ = ['murmurhash3', 'lookup3', 'mmh3']


class LogLogEstimator(DistinctCounterEstimator):

    def __init__(self,
                 num_buckets: int,
                 seed: int = random.randint(-214783648, 2147483647)) -> None:
        self.num_bits = int(math.log(num_buckets, 2))
        self.seed = seed
        self.num_buckets = num_buckets
        self.max_hash_value_by_buckets = [0] * (2**self.num_bits)
        self.correction_factor = [0, 0.44567926005415, 1.2480639342271, 2.8391255240079, 6.0165231584809,
                                  12.369319965552, 25.073991603111, 50.482891762408, 101.30047482584, 202.93553338100,
                                  406.20559696699, 812.74569744189, 1625.8258850594, 3251.9862536323, 6504.3069874480,
                                  13008.948453415, 26018.231384516, 52036.797246302, 104073.92896967, 208148.19241629,
                                  416296.71930949, 832593.77309585, 1665187.8806686, 3330376.0958140, 6660752.5261049,
                                  13321505.386687, 26643011.107850, 53286022.550177, 106572045.43483, 213144091.20414,
                                  426288182.74275, 852576365.81999]
        self.hash_function_upper_bound = 2**63 - 1
        assert self.num_bits < len(self.correction_factor)

    def increment(self, element: object) -> None:
        element_str = str(element).encode('utf-8')
        h = smhasher.murmur3_x64_64(element_str) % self.hash_function_upper_bound
        bucket_idx = self.get_bucket_id(h)
        self.max_hash_value_by_buckets[bucket_idx] = max(self.max_hash_value_by_buckets[bucket_idx],
                                                         self.count_leading_zeros(h))

    def get_bucket_id(self, hash_value: int) -> int:
        binary_str = bin(hash_value)[2:][-self.num_bits:]
        return int(binary_str, 2)

    def count_leading_zeros(self, hash_value: int) -> int:
        binary_str = bin(hash_value)[2:][0:-self.num_bits]
        count = 0
        idx = len(binary_str) - 1
        while idx < len(binary_str) and binary_str[idx] == '0':
            idx = idx - 1
            count += 1
        return count + 1

    def approx_distinct_count(self) -> float:
        total_sum = sum(self.max_hash_value_by_buckets)
        total_buckets = len(self.max_hash_value_by_buckets)
        mean_value = total_sum / float(total_buckets)
        return self.correction_factor[self.num_bits] * (2 ** mean_value)
