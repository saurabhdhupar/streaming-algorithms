import unittest
from distinct_count.flajolet_martin.flajolet_martin_extension_one import FlajoletMartinMeanEstimator


class FlajoletMartinMeanEstimatorTest(unittest.TestCase):

    def test_flajolet_martin(self):
        counter = FlajoletMartinMeanEstimator(32, 24)
        for i in range(10000):
            counter.increment(i)
            if i % 1000 == 0:
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(counter.approx_distinct_count()))
