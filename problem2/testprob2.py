import unittest
from problem2.prob2 import *

class TestProb2(unittest.TestCase):

    def test_working(self):
        self.assertEqual(True, True)

    def test_rectangle_1(self):
        self.assertEqual("Area: 20 units and Perimeter: 18 units", p2())

    def test_rectangle_2(self):
        self.assertEqual("Area: 20 units and Perimeter: 18 units", p2())


if __name__ == '__main__':
    unittest.main()
