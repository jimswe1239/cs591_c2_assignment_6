import unittest
from problem4 import *


class ProblemFourTest(unittest.TestCase):
    def test_working(self):
        self.assertEqual(True, True)

    def test_lessthanzero1(self):
        self.assertEqual(p4(-1), 0)
    
    def test_lessthanten1(self):
        self.assertEqual(p4(-18), 0)

    def test_zero(self):
        self.assertEqual(p4(0), 0)
    
    def test_one(self):
        self.assertEqual(p4(1), 1)
    
    def test_lessthanten1(self):
        self.assertEqual(p4(4), 1)

    def test_lessthanten2(self):
        self.assertEqual(p4(7), 1)
    
    def test_lessthantwenty1(self):
        self.assertEqual(p4(17), 10)

    def test_lessthantwenty2(self):
        self.assertEqual(p4(18), 11)

    def test_lessthanhundred1(self):
        self.assertEqual(p4(52), 16)

    def test_lessthanhundred2(self):
        self.assertEqual(p4(78),18)

    def test_lessthanthousand1(self):
        self.assertEqual(p4(111), 36)

    def test_lessthanthousand2(self):
        self.assertEqual(p4(234), 154)



if __name__ == '__main__':
    unittest.main()
