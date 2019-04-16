import unittest

from babysitter import calculate


class FamilyATest(unittest.TestCase):

    def test_babysitter_works_1_hour_family_A(self):
        self.assertEqual(15, calculate(17, 18, "Family A"))

    def test_babysitter_works_first_half_family_A(self):
        self.assertEqual(6 * 15, calculate(17, 23, "Family A"))

    def test_babysitter_works_second_half_family_A(self):
        self.assertEqual(5*20, calculate(23, 4, "Family A"))

    def test_babysitter_works_full_shift_family_A(self):
        self.assertEqual(6 * 15 + 5 * 20, calculate(17, 4, "Family A"))


class FamilyBTest(unittest.TestCase):

    def test_babysitter_works_1_hour_family_B(self):
        self.assertEqual(12, calculate(17, 18, "Family B"))

    def test_babysitter_works_shift_1_family_B(self):
        self.assertEqual(60, calculate(17, 22, "Family B"))

    def test_babysitter_works_shift_2_family_B(self):
        self.assertEqual(16, calculate(22, 24, "Family B"))

    def test_babysitter_works_shift_3_family_B(self):
        self.assertEqual(16 * 4, calculate(0, 4, "Family B"))

    def test_babysitter_works_full_shift_family_B(self):
        self.assertEqual(60 + 16 + 64, calculate(17, 4, "Family B"))


class FamilyCTest(unittest.TestCase):

    def test_babysitter_works_1_hour_family_C(self):
        self.assertEqual(21, calculate(17, 18, "Family C"))

    def test_babysitter_works_shift_1_family_C(self):
        self.assertEqual(84, calculate(17, 21, "Family C"))

    def test_babysitter_works_shift_2_family_C(self):
        self.assertEqual(105, calculate(21, 4, "Family C"))

    def test_babysitter_works_full_shift_family_C(self):
        self.assertEqual(189, calculate(17, 4, "Family C"))

    def test_babysitter_works_full_shift_family_C(self):
        self.assertRaises(Exception, calculate, 16, 20, "Family C")
