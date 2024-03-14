import unittest
from main import generate_bbs_sequence

class TestBBS(unittest.TestCase):
    def test_monobit(self):
        sequence = generate_bbs_sequence(20000)
        num_ones = sequence.count(1)
        lower_bound = 9725
        upper_bound = 10275
        self.assertTrue(lower_bound <= num_ones <= upper_bound)

    def test_poker(self):
        #sequence = generate_bbs_sequence(20000)
        # Implementacja testu pokerowego FIPS 140-2
        pass

    def test_runs(self):
        # Implementacja testu długich serii FIPS 140-2
        pass

    def test_autocorrelation(self):
        # Implementacja testu autokorelacji FIPS 140-2
        pass

if __name__ == '__main__':
    unittest.main()