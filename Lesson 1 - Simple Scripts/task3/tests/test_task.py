import unittest

from task3 import compare_two_variables


class TestCase(unittest.TestCase):
    def test_compare(self):
        m1 = "string involved"
        m2 = "bigger"
        m3 = "smaller"
        m4 = "equal"
        self.assertEqual(m1, compare_two_variables(-7, "adieu"))
        self.assertEqual(m3, compare_two_variables(3, 8))
        self.assertEqual(m2, compare_two_variables(5, -9))
        self.assertEqual(m4, compare_two_variables(-5, -5))
        self.assertEqual(m2, compare_two_variables(7, -2))
        self.assertEqual(m1, compare_two_variables("hola", "adieu"))
        self.assertEqual(m2, compare_two_variables(5, -3))
        self.assertEqual(m1, compare_two_variables(0, "adieu"))
        self.assertEqual(m3, compare_two_variables(-10, -9))
        self.assertEqual(m1, compare_two_variables("hello", -7))
