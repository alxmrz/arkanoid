import unittest
from unittest.mock import Mock
from src.Scene import *

class SceneTest(unittest.TestCase):

    def setUp(self):
        self.myc = Scene()

    def tearDown(self):
        self.myc = None

    def testSum(self):
        assert self.myc.sum(5, 5) == 10, 'incorrect sum'

if __name__ == "__main__":
    unittest.main()
