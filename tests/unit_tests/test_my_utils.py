import sys
import unittest
import numpy as np
import random

sys.path.append('src')  # noqa

import my_utils as mu


class TestMyUtils(unittest.TestCase):

    def test_find_mean(self):
        data1 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(mu.find_mean(data1), 3.5)
        self.assertNotEqual(mu.find_mean(data1), 4)

        data2 = [random.uniform(0, 1000) for i in range(100)]
        np_mean = np.mean(data2)
        my_mean = mu.find_mean(data2)
        self.assertAlmostEqual(np_mean, my_mean, places=3)

    def test_find_median(self):
        data1 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(mu.find_median(data1), 3.5)
        self.assertNotEqual(mu.find_median(data1), 3)
        self.assertNotEqual(mu.find_median(data1), 4)

        data2 = [random.uniform(0, 1000) for i in range(101)]
        np_median = np.median(data2)
        my_median = mu.find_median(data2)
        self.assertAlmostEqual(np_median, my_median, places=3)

        data3 = [random.uniform(0, 1000) for i in range(101)]
        np_median = np.median(data3)
        my_median = mu.find_median(data3)
        self.assertAlmostEqual(np_median, my_median, places=3)

    def test_find_stddev(self):
        data1 = [1, 2, 3, 4, 5, 6]
        self.assertAlmostEqual(mu.find_stddev(data1), 1.7078, places=3)
        self.assertNotEqual(mu.find_stddev(data1), 2)

        data2 = [random.uniform(0, 1000) for i in range(100)]
        np_stddev = np.std(data2)
        my_stddev = mu.find_stddev(data2)
        self.assertAlmostEqual(np_stddev, my_stddev, places=3)


if __name__ == '__main__':
    unittest.main()
