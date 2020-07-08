import unittest

from distinct_count.loglog.loglog import LogLogEstimator
from distinct_count.superloglog.superloglog import SuperLogLogEstimator


class SuperLogLogEstimatorTest(unittest.TestCase):

    def test_super_loglog_estimator(self):
        counter = SuperLogLogEstimator(num_buckets=1024)
        for i in range(10000):
            counter.increment(i)
            if i % 100 == 0:
                print("Total Elements : " + str(i) + " vs Approx Count :: " + str(counter.approx_distinct_count()))
