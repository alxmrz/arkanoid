import unittest
from unittest.mock import Mock
from src.Application import *

class ApplicationTest(unittest.TestCase):

    another = None

    def setUp(self):
        self.myc = Application()

    def tearDown(self):
        self.myc = None

    def testSum(self):
        assert self.myc.sum(5, 5) == 10, 'incorrect sum'

    def testMinus(self):
        assert self.myc.minus(6,5) == 1, 'incorrect minus'

    def testAnotherSum(self):
        self.another.makeIt.return_value = 5
        assert self.myc.anotherSum() == 10

        self.another.makeIt.return_value = 10
        assert self.myc.anotherSum() == 101

if __name__ == "__main__":
    unittest.main()
