from distinct_count.distinct_count import DistinctCounterEstimator
import math
from bitarray import bitarray
import pyhash
import smhasher
from hashlib import md5

_HASH_FUNCTIONS_ = ['murmurhash3', 'lookup3']


class LinearCounter(DistinctCounterEstimator):

    def __init__(self, bitmap_size: int, hashing_function: str = 'murmurhash3') -> None:
        self.bitmap_size = bitmap_size
        self.bit_map = bitarray(bitmap_size)
        self.bit_map.setall(False)
        assert hashing_function in _HASH_FUNCTIONS_
        self.hashing_function = hashing_function

    def increment(self, element: object):
        element_str = str(element).encode('utf-8')
        if self.hashing_function == 'murmurhash3':
            offset = smhasher.murmur3_x64_128(element_str) % self.bitmap_size
        else:
            hasher = pyhash.lookup3()
            offset = hasher(element_str) % self.bitmap_size
        self.bit_map[offset] = True

    def approx_distinct_count(self) -> float:
        total_unset_bits_in_bitmap = self.bit_map.count(False)
        ratio = total_unset_bits_in_bitmap / self.bitmap_size
        return -self.bitmap_size * math.log(ratio)
