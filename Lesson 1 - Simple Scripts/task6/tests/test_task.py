import unittest

from task6 import sum_range


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(45, sum_range(9), msg="Adds numbers from 1 to 9")
        self.assertEqual(190, sum_range(19), msg="Adds numbers from 1 to 19")
        self.assertEqual(136, sum_range(16), msg="Adds numbers from 1 to 16")
