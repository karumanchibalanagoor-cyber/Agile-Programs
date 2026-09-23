import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertAlmostEqual(calculator.add(2,3),5)
        self.assertAlmostEqual(calculator.add(-1,-1),-2)
        self.assertAlmostEqual(calculator.add(0,0),0)
    def test_subtract(self):
        self.assertAlmostEqual(calculator.subtract(10,5),5)
        self.assertAlmostEqual(calculator.subtract(0,7),-7)
        self.assertAlmostEqual(calculator.subtract(7,0),7)
    def test_multiply(self):
        self.assertAlmostEqual(calculator.multiply(3,4),12)
        self.assertAlmostEqual(calculator.multiply(-2,5),-10)
        self.assertAlmostEqual(calculator.multiply(0,5),0)
    def test_divide(self):
        self.assertAlmostEqual(calculator.divide(10,2),5)
        self.assertAlmostEqual(calculator.divide(9,3),3)
        self.assertAlmostEqual(calculator.divide(1,3),0.333333, places=6)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10,0)

if __name__=="__main__":
    unittest.main()