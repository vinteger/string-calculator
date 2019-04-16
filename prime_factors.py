import unittest


class PrimeFactorsTest(unittest.TestCase):
    def setUp(self):
        self.prime_factors = PrimeFactors()

    def test_2_returns_list_with_2(self):
        self.assertEqual([2], self.prime_factors.check_numbers(2), "2 as arg")

    def test_3_returns_empty_list(self):
        self.assertEqual([3], self.prime_factors.check_numbers(3), "3 as arg")

    def test_4_returns_list_with_2_2(self):
        self.assertEqual([2, 2], self.prime_factors.check_numbers(4))

    def test_5_returns_list(self):
        self.assertEqual([5], self.prime_factors.check_numbers(5))

    def test_6_returns_list(self):
        self.assertEqual([2, 3], self.prime_factors.check_numbers(6))

    def test_9_returns_list_with_3_3(self):
        self.assertEqual([3, 3], self.prime_factors.check_numbers(9))

    def test_10_returns_list_with_2_5(self):
        self.assertEqual([2, 5], self.prime_factors.check_numbers(10))

    def test_12_returns_list_with_2_2_3(self):
        self.assertEqual([2, 2, 3], self.prime_factors.check_numbers(12))

    def test_25_returns_list_with_5_5(self):
        self.assertEqual([5,5], self.prime_factors.check_numbers(25))

    def test_30_returns_list_with_2_3_5(self):
        self.assertEqual([2,3,5], self.prime_factors.check_numbers(30))

    def test_42_returns_list_with_2_3_7(self):
        self.assertEqual([2,3,7], self.prime_factors.check_numbers(42))

    def test_really_big_number(self):
        self.assertEqual([2, 36871, 4436947], self.prime_factors.check_numbers(327189345674))



class PrimeFactors:

    def check_numbers(self, number):
        if number < 2:
            return []

        divisors = []

        divisor = 2
        while number >= 2:
            if number % divisor == 0:
                divisors.append(divisor)
                number /= divisor
            else:
                divisor += 1

        return divisors
