import unittest

from approx_counting.morris_algorithm import MorrisAlgorithm


class MorrisAlgorithmTest(unittest.TestCase):

    def test_morris_algorithm(self):
        count_approx = MorrisAlgorithm()
        for i in range(100000):
            count_approx.increment()
            if i % 1000 == 0:
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(count_approx.approx_count()))
