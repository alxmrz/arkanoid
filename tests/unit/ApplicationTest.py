import unittest
from unittest.mock import Mock
from src.Application import *
"""
There is no tests until i find a way to avoid infinity loop
"""
class ApplicationTest(unittest.TestCase):

    another = None

    def setUp(self):
        self.myc = Application()

    def tearDown(self):
        self.myc = None


if __name__ == "__main__":
    unittest.main()
