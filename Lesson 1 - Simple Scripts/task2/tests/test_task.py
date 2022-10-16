import unittest

from task2 import print_if_happy


class TestCase(unittest.TestCase):
    word = "hello world"

    def test_add(self):
        self.assertEqual(None, print_if_happy(1), msg="happy is equal to 1, it shouldn't return anything, comparison: ")
        self.assertEqual(None, print_if_happy(2), msg="happy is equal to 2, it shouldn't return anything, comparison: ")
        self.assertEqual(self.word, print_if_happy(3), msg="happy is equal to 3, it should return \"hello world\", comparison: ")
        self.assertEqual(self.word, print_if_happy(4), msg="happy is equal to 4, it should return \"hello world\", comparison: ")
        self.assertEqual(None, print_if_happy(-25), msg="happy is equal to -25, it shouldn't return anything, comparison: ")
        self.assertEqual(None, print_if_happy(-96), msg="happy is equal to -96, it shouldn't return anything, comparison: ")
        self.assertEqual(None, print_if_happy(-23), msg="happy is equal to -23, it shouldn't return anything, comparison: ")
        self.assertEqual(self.word, print_if_happy(43), msg="happy is equal to 43, it should return \"hello world\", comparison: ")
        self.assertEqual(None, print_if_happy(-18), msg="happy is equal to -18, it shouldn't print anything, comparison: ")
        self.assertEqual(self.word, print_if_happy(93), msg="happy is equal to 93, it should return \"hello world\", comparison: ")

