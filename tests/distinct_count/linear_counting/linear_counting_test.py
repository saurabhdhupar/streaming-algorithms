import unittest

from distinct_count.linear_counting.linear_counter import LinearCounter


class LinearCounterTest(unittest.TestCase):

    def test_linear_counter(self):
        size_kb = 32768
        counter = LinearCounter(size_kb * 1024 * 8)
        for i in range(100000):
            counter.increment(i)
            if i % 1000 == 0:
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(counter.approx_distinct_count()))
