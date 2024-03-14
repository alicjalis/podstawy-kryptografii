import unittest
from main import generate_bbs_sequence


class TestBBS(unittest.TestCase):
    def test_monobit(self):
        sequence = generate_bbs_sequence(20000)
        num_ones = sequence.count(1)
        lower_bound = 9725
        upper_bound = 10275
        self.assertTrue(lower_bound <= num_ones <= upper_bound)

    def test_series(self):
        # sequence = generate_bbs_sequence(20000)
        # Implementacja testu pokerowego FIPS 140-2
        pass

    def test_long_series(self):
        threshold = 26
        current_zeros = 0
        current_ones = 0
        sequence = generate_bbs_sequence(20000)
        for bit in sequence:
            if bit == 0:
                current_zeros += 1
                current_ones = 0
                if current_zeros >= threshold:
                    self.assertFalse(True, "Znaleziono długą serię zer")
            if bit == 1:
                current_zeros = 0
                current_ones += 1
                if current_ones >= threshold:
                    self.assertFalse(True, "Znaleziono długą serię jedynek")


        self.assertTrue(True)

    def test_poker(self):
        # Implementacja testu autokorelacji FIPS 140-2
        pass


if __name__ == '__main__':
    unittest.main()
