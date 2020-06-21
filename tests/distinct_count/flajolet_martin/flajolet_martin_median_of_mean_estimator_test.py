import unittest
from distinct_count.flajolet_martin.flajolet_martin_algorithm import FlajoletMartinAlgorithm
from distinct_count.flajolet_martin.flajolet_martin_extension_one import FlajoletMartinMeanEstimator
from distinct_count.flajolet_martin.flajolet_martin_extension_two import FlajoletMartinMedianOfMeanEstimator


class FlajoletMartinMedianOfMeanEstimatorTest(unittest.TestCase):

    def test_flajolet_martin(self):
        counter = FlajoletMartinMedianOfMeanEstimator(24, 24, 24)
        for i in range(100000):
            counter.increment(i)
            if i % 1000 == 0:
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(counter.approx_distinct_count()))
