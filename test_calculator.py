import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(calculator.sqrt(16), 4)
        self.assertEqual(calculator.sqrt(0), 0)
        self.assertAlmostEqual(calculator.sqrt(2), 1.41421356, places=8)

    def test_fact(self):
        self.assertEqual(calculator.fact(5), 120)
        self.assertEqual(calculator.fact(0), 1)
        self.assertEqual(calculator.fact(1), 1)

    def test_log(self):
        self.assertAlmostEqual(calculator.log(1), 0)
        # math.e is approx 2.71828, so ln(math.e) should be 1
        self.assertAlmostEqual(calculator.log(2.71828), 1, places=5)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)
        self.assertEqual(calculator.power(-2, 2), 4)
        self.assertAlmostEqual(calculator.power(4, 0.5), 2)

if __name__ == '__main__':
    unittest.main()