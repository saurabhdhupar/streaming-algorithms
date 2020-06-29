import unittest
from distinct_count.flajolet_martin.flajolet_martin_extension_one import FlajoletMartinMeanEstimator
from distinct_count.kmv.kmv_sketch_extension_one import KMVSketchMeanEstimator


class KMVSketchMeanEstimatorTest(unittest.TestCase):

    def test_kmv_sketch(self):
        counter = KMVSketchMeanEstimator(total_estimators=32)
        for i in range(10000):
            counter.increment(i)
            if i % 100 == 0:
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(counter.approx_distinct_count()))
