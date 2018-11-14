import unittest
import sys
from unittest.mock import Mock, MagicMock

sys.modules['pygame'] = MagicMock()
import pygame

from src.Ball import *
from tests.GeneralTest import *
from src.UI import *


class BallTest(GeneralTest):

    def setUp(self):
        self.ball = Ball(self._mock_app(), (0, 0))

    def tearDown(self):
        self.ball = None

    def test_change_direction_border(self):
        self.ball.change_direction_border()
        self.assertEqual(self.ball.speed, [0, -1], 'Initial state does not change when coords is (0,0)')

        self.ball.speed = [-1, -1]
        self.ball.x = -1
        self.ball.change_direction_border()
        self.assertEqual(self.ball.speed, [1, -1], 'When x is less then zero change x')

        self.ball.speed = [1, -1]
        self.ball.x = self.width + 1
        self.ball.change_direction_border()
        self.assertEqual(self.ball.speed, [-1, -1], 'When x is more then width change x')

        self.ball.speed = [1, -1]
        self.ball.x = 1
        self.ball.y = -1
        self.ball.change_direction_border()
        self.assertEqual(self.ball.speed, [1, 1], 'When y is less then zero change y')

    def test_change_direction_platform(self):
        self.ball.x = 100
        self.ball.change_direction_platform()
        self.assertEqual(self.ball.speed, [-2, -1], 'First quarter must return the next direction: [-2, -1]')

        self.ball.x = 130
        self.ball.change_direction_platform()
        self.assertEqual(self.ball.speed, [-1, -1], 'Second quarter must return the next direction: [-1, -1]')

        self.ball.x = 160
        self.ball.change_direction_platform()
        self.assertEqual(self.ball.speed, [1, -1], 'Third quarter must return the next direction: [1, -1]')

        self.ball.x = 190
        self.ball.change_direction_platform()
        self.assertEqual(self.ball.speed, [2, -1], 'Fourth quarter must return the next direction: [2, -1]')

if __name__ == "__main__":
    unittest.main()
