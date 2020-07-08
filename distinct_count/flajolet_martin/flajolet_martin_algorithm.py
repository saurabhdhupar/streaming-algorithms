import random
from datetime import datetime
from bitarray import bitarray
import pyhash
import smhasher
import mmh3


from distinct_count.distinct_count import DistinctCounterEstimator

_HASH_FUNCTIONS_ = ['murmurhash3', 'lookup3', 'mmh3']


class FlajoletMartinAlgorithm(DistinctCounterEstimator):

    def __init__(self, sketch_size: int,
                 seed: int = random.randint(-214783648, 2147483647),
                 hashing_function: str = 'murmurhash3') -> None:
        self.sketch_size = sketch_size
        self.hash_function_upper_bound = 2**sketch_size - 1
        self.bitmap = bitarray(sketch_size)
        self.bitmap.setall(False)
        assert hashing_function in _HASH_FUNCTIONS_
        self.hashing_function = hashing_function
        self.correction_factor = 0.77351
        self.seed = seed

    def increment(self, element: object) -> None:
        element_str = str(element).encode('utf-8')
        if self.hashing_function == 'murmurhash3':
            h = smhasher.murmur3_x64_128(element_str, self.seed) % self.hash_function_upper_bound
        elif self.hashing_function == 'mmh3':
            h = mmh3.hash(element_str, seed=self.seed) % self.hash_function_upper_bound
        else:
            hasher = pyhash.lookup3()
            h = hasher(element_str, str(self.seed)) % self.hash_function_upper_bound
        self.bitmap[self.count_trailing_zeros(h, self.sketch_size)] = True

    @staticmethod
    def count_trailing_zeros(num: int, sketch_size: int):
        if num == 0:
            return sketch_size - 1
        binary_str = bin(num)[2:].zfill(sketch_size)
        i = len(binary_str) - 1
        cnt = 0
        while i >= 0 and binary_str[i] == '0':
            cnt += 1
            i = i - 1
        return cnt

    def get_max_value(self) -> float:
        r_index = 0
        while self.bitmap[r_index] is not False and r_index < self.sketch_size - 1:
            r_index += 1
        return r_index

    def approx_distinct_count(self) -> float:
        r_index = self.get_max_value()
        return 2**r_index / self.correction_factor
