import unittest
from unittest.mock import patch
from io import StringIO
from task1 import show_on_screen


class TestCase(unittest.TestCase):
    def test_printed(self):
        expected = "hello world"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            show_on_screen()
            self.assertEqual(fake_out.getvalue().strip("\n"), expected, msg="show the printed text \"hello world\"")
