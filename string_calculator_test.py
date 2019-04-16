import unittest

from string_calculator import StringCalculator


class StringCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.string_calculator = StringCalculator()

    def test_empty_string_returns_0(self):
        self.assertEqual(0, self.string_calculator.add(""))

    def test_1_string_returns_1(self):
        self.assertEqual(1, self.string_calculator.add("1"))

    def test_1_and_2_sum_returns_3(self):
        self.assertEqual(3, self.string_calculator.add("1,2"))

    def test_10_and_10_returns(self):
        self.assertEqual(20, self.string_calculator.add("10,10"))

    def test_10_10_and_10_returns_30(self):
        self.assertEqual(30, self.string_calculator.add("10,10,10"))

    def test_1_newline_2_3_returns_6(self):
        self.assertEqual(6, self.string_calculator.add("1\n2,3"))

    def test_can_have_semicolon_delimiter(self):
        self.assertEqual(3, self.string_calculator.add("//;\n1;2"))

    def test_can_not_have_negative_numbers(self):
        self.assertRaisesRegex(ValueError, "negatives not allowed: -3", self.string_calculator.add, "1\n2,-3")

    def test_show_all_negatives_in_exception(self):
        self.assertRaisesRegex(ValueError, "negatives not allowed: -2, -3", self.string_calculator.add, "1\n-2,-3")

    def test_ignore_numbers_bigger_than_1000(self):
        self.assertEqual(2, self.string_calculator.add("2,1001"))

    def test_big_delimiter(self):
        self.assertEqual(6, self.string_calculator.add("//[***]\n1***2***3"))

    def test_can_handle_multiple_delimiters(self):
        self.assertEqual(6, self.string_calculator.add("//[*][%]\n1*2%3"))

    def test_can_handle_multiple_delimiters_with_longer_characters(self):
        self.assertEqual(6, self.string_calculator.add("//[**][%%%]\n1**2%%%3"))