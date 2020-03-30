import unittest
from problem1 import *


class ProblemOneTest(unittest.TestCase):
    def test_working(self):
        self.assertEqual(True, True)

    def test_io(self):
        self.assertEqual(p1(""), {"protocol": "", "domain": "", "path": ""})

    def test_protocol1(self):
        self.assertEqual(p1("http://"), {"protocol": "http", "domain": "", "path": ""})

    def test_protocol2(self):
        self.assertEqual(p1("ftp://"), {"protocol": "ftp", "domain": "", "path": ""})

    def test_domain1(self):
        self.assertEqual(p1("www.google.com"), {"protocol": "", "domain": "www.google.com", "path": ""})

    def test_domain2(self):
        self.assertEqual(p1("bu.edu/"), {"protocol": "", "domain": "bu.edu", "path": ""})

    def test_path1(self):
        self.assertEqual(p1("/some-path"), {"protocol": "", "domain": "", "path": "some-path"})

    def test_path2(self):
        self.assertEqual(p1("/"), {"protocol": "", "domain": "", "path": ""})

    def test_full1(self):
        self.assertEqual(p1("https://www.google.com/some-path"), {"protocol": "https", "domain": "www.google.com", "path": "some-path"})

    def test_full2(self):
        self.assertEqual(p1("ftp://bu.edu/"), {"protocol": "ftp", "domain": "bu.edu", "path": ""})


if __name__ == '__main__':
    unittest.main()
