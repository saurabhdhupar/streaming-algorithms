import unittest

from distinct_count.kmv.kmv_sketch import KMVSketch


class KMVSketchTest(unittest.TestCase):

    def test_kmv_sketch(self):
        counter = KMVSketch()
        for i in range(10000):
            counter.increment(i)
            if i % 100 == 0:
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(counter.approx_distinct_count()))
