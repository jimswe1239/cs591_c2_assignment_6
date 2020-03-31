import unittest
from problem2.prob2 import *

class TestProb2(unittest.TestCase):

    def test_working(self):
        self.assertEqual(True, True)

    def test_rectangle_1(self):
        #input R then 4 then 5
        self.assertEqual("Area: 20 units and Perimeter: 18 units", p2("R", 4, 5))

    def test_rectangle_2(self):
        #input R then 5 then 10
        self.assertEqual("Area: 50 units and Perimeter: 30 units", p2("R", 5, 10))

    def test_square_1(self):
        #input S then 6 then 6
        self.assertEqual("Area: 36 units and Perimeter: 24 units", p2("S", 6, 6))

    def test_square_2(self):
        #input S then 7 then 7
        self.assertEqual("Area: 49 units and Perimeter: 28 units", p2("S", 7, 7))

    def test_circle_1(self):
        #input C then 5 then 5
        self.assertEqual("Area: 78.53981633974483 units and Perimeter: 31.41592653589793 units", p2("C", 5, 5))

    def test_circle_2(self):
        #input C then 7 then 7
        self.assertEqual("Area: 153.93804002589985 units and Perimeter: 43.982297150257104 units", p2("C", 7, 7))

if __name__ == '__main__':
    unittest.main()
