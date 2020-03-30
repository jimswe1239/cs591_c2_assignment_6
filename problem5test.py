from problem5 import *
import unittest

class ProblemOneTest(unittest.TestCase):
    
    def testWorking(self):
        self.assertEqual(True, True)

    def testCompare1(self):
        self.assertEqual(isMoreThan2xGreater(3, 1), True)

    def testCompare2(self):
        self.assertEqual(isMoreThan2xGreater(1, 2), False)

    def testEmptyStr(self):
        self.assertEqual(problem5([]), 0)

    def testOneVal(self):
        self.assertEqual(problem5([1]), 0)

    def testEx0(self):
        self.assertEqual(problem5([0,0,0,0,0,0,0,0,0]), 0)

    def testEx1(self):
        self.assertEqual(problem5([1,3,2,3,1]), 2)

    def testEx2(self):
        self.assertEqual(problem5([2,4,3,5,1]), 3)
        
    def testEx3(self):
        self.assertEqual(problem5([1,2,3,4,5]), 0)

    def testEx4(self):
        self.assertEqual(problem5([31, 15, 7, 3, 1]), 10)

    def testEx5(self):
        self.assertEqual(problem5([-1, -2, -3, -4, -5]), 10)

    def testEx6(self):
        self.assertEqual(problem5([-31, -15, -7, -3, -1]), 0)
    

if __name__ == '__main__':
    unittest.main()
