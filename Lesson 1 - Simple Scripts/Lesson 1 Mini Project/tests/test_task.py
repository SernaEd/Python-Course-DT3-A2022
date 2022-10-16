import unittest
from unittest.mock import patch
from finalTask import find_secret_number


class TestCase(unittest.TestCase):
    string_of_inputs = "l l h l h l c"

    @patch('builtins.input', side_effect=['l', 'l', 'h', 'l', 'h', 'l', 'c'])
    def test_secret_number_83(self, mock_input):
        guessed_number = find_secret_number(0, 100)
        self.assertEqual(guessed_number, 83)

    @patch('builtins.input', side_effect=['h', 'l', 'l', 'h', 'l', 'l', 'c'])
    def test_secret_number_42(self, mock_input):
        guessed_number = find_secret_number(0, 100)
        self.assertEqual(guessed_number, 42)

    @patch('builtins.input', side_effect=['l', 'l', 'l', 'h', 'l', 'y', 'c'])
    def test_secret_number_91(self, mock_input):
        guessed_number = find_secret_number(0, 100)
        self.assertEqual(guessed_number, 91)

    @patch('builtins.input', side_effect=['h', 'h', 'h', 'l', 'h', 'l', 'c'])
    def test_secret_number_8(self, mock_input):
        guessed_number = find_secret_number(0, 100)
        self.assertEqual(guessed_number, 8)

    @patch('builtins.input',
           side_effect=['l', 'h', 'l', 'right', 'correct', 'yes', 'okay', 'yes that is my guess', 'c'])
    def test_secret_number_68(self, mock_input):
        guessed_number = find_secret_number(0, 100)
        self.assertEqual(guessed_number, 68)
