import unittest

from distinct_count.flajolet_martin.flajolet_martin_extension_two import FlajoletMartinMedianOfMeanEstimator


class FlajoletMartinMedianOfMeanEstimatorTest(unittest.TestCase):

    def test_flajolet_martin(self):
        counter = FlajoletMartinMedianOfMeanEstimator(32, 24, 24, hashing_function='mmh3')
        for i in range(5000):
            counter.increment(i)
            if i > 0 and i % 100 == 0:
                error = (i - counter.approx_distinct_count()) * 100 / i
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(counter.approx_distinct_count()))
                print("Error : " + str(error))
