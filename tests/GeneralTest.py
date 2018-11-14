import unittest
import sys
from unittest.mock import Mock, MagicMock
from src.Application import *


class GeneralTest(unittest.TestCase):
    width = 900
    height = 600

    def _mock_app(self):
        ball = Mock()
        ball.draw = MagicMock()

        platform = Mock()
        platform.x = 100
        platform.draw = MagicMock()

        plate = Mock()
        plate.draw = MagicMock()


        app = MagicMock(Application)

        app.ball = ball
        app.platform = platform
        app.game_objects = {
            'ball': ball,
            'platform': platform,
            'plates': [plate],
        }
        app.game_over = False
        app.game_started = True

        window = Mock()
        window.width = self.width
        window.height = self.height
        app.window = window

        return app

