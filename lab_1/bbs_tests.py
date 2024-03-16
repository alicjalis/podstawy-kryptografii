import unittest
from main import generate_bbs_sequence


class TestBBS(unittest.TestCase):
    def test_monobit(self):
        sequence = generate_bbs_sequence(20000)
        num_ones = sequence.count('1')
        lower_bound = 9725
        upper_bound = 10275
        self.assertTrue(lower_bound <= num_ones <= upper_bound)

    def test_series(self):
        sequence = generate_bbs_sequence(20000)
        freq, prev = 0, sequence[0]
        arr = [[0] * 6 for _ in range(2)]
        for c in sequence:
            if prev == c:
                freq += 1
            else:
                if freq < 6:
                    arr[int(prev)][freq - 1] += 1
                else:
                    arr[int(prev)][5] += 1
                prev = c
                freq = 1
        if freq < 6:
            arr[int(prev)][freq - 1] += 1
        else:
            arr[int(prev)][5] += 1

        self.assertTrue(2315 <= arr[0][0] <= 2685 and 2315 <= arr[1][0] <= 2685)
        self.assertTrue(1114 <= arr[0][1] <= 1386 and 1114 <= arr[1][1] <= 1386)
        self.assertTrue(527 <= arr[0][2] <= 723 and 527 <= arr[1][2] <= 723)
        self.assertTrue(240 <= arr[0][3] <= 384 and 240 <= arr[1][3] <= 384)
        self.assertTrue(103 <= arr[0][4] <= 209 and 103 <= arr[1][4] <= 209)
        self.assertTrue(103 <= arr[0][5] <= 209 and 103 <= arr[1][5] <= 209)

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

        self.assertTrue(True, "Brak długich serii")

    def test_poker(self):
        sequence = generate_bbs_sequence(20000)
        arr, i, length = [0] * 16, 0, len(sequence)
        while i < length - 4:
            arr[int(sequence[i:i + 4], 2)] += 1
            i += 4
        x = 16 / 5000
        for i in range(0, 16):
            x *= pow(arr[i], 2) - 5000
        if x < 2.16 and x > 46.17:
            self.assertFalse("Poker test failed, x = " + str(x))
        else:
            self.assertTrue("Poker test passed")


if __name__ == '__main__':
    unittest.main()
