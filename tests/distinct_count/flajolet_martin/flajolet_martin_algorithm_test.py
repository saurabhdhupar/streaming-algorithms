import unittest
from distinct_count.flajolet_martin.flajolet_martin_algorithm import FlajoletMartinAlgorithm


class FlajoletMartinAlgorithmTest(unittest.TestCase):

    def test_flajolet_martin(self):
        counter = FlajoletMartinAlgorithm(24)
        for i in range(10000):
            counter.increment(i)
            if i % 100 == 0:
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(counter.approx_distinct_count()))
