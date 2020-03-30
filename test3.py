import unittest
from problem3 import *


class ProblemOneTest(unittest.TestCase):
    def test_working(self):
        self.assertEqual(True, True)

    def test_zeroMultiplication(self):
        self.assertEqual(p3("0", "0"), "0")

    def test_oneMultiplication(self):
        self.assertEqual(p3("1", "1"), "1")

    def test_StringtoIntHelper(self):
        self.assertEqual(stringToInt(["5"]), 5)

    def test_StringtoIntTwoDigitsHelper(self):
        self.assertEqual(stringToInt(["1", "5"]), 15)

    def test_inttostringHelper(self):
        self.assertEqual(intToString(1), "1")

    def test_inttostringTwoDigitsHelper(self):
        self.assertEqual(intToString(10), "10")

    def test_twoDigitMultiplication(self):
        self.assertEqual(p3("10", "6"), "60")

    def test_twoDigitMultiplication(self):
        self.assertEqual(p3("10", "15"), "150")

    def test_twoHarderDigitMultiplication(self):
        self.assertEqual(p3("13", "59"), "767")

if __name__ == '__main__':
    unittest.main()

