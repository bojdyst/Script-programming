import main
import unittest


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_rational_rational(self):
        self.assertEqual(main.sum(7/6, 4/15), 43/30)

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(5 + 4j, 3 - 1j), 8 + 3j)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(ValueError):
            main.sum(2, 'Ala ma kota123')

    def test_sum_integer_neither_number_nor_string(self):
        with self.assertRaises(TypeError):
            main.sum(1, [2, 3])


if __name__ == "__main__":
    unittest.main()