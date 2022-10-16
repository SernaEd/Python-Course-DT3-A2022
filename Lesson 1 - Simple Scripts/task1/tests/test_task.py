import unittest

with open("task.txt") as f:
    lines = f.readlines()


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual("print(\"hello world\")", lines[0].removesuffix("\n"), msg="show the printed text \"hello world\"")
