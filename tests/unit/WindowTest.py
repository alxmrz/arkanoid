import unittest
import sys
from unittest.mock import Mock, MagicMock

sys.modules['pygame'] = MagicMock()
import pygame

from src.Window import *
from tests.GeneralTest import *
from src.UI import *


class WindowTest(GeneralTest):

    def setUp(self):

        self.window = Window(self._mock_app(), 900, 600, 'Title')
        self.window.UI = MagicMock(UI)


    def tearDown(self):
        self.window = None

    def test_display(self):
        screen = Mock()

        screen.fill = MagicMock()
        self.window.screen = screen

        self.window.display()

        self.window.screen.fill.assert_called_with(self.window.colors['black'])
        self.window.app.game_objects['ball'].draw.assert_called()
        self.window.app.game_objects['platform'].draw.assert_called()
        self.window.app.game_objects['plates'][0].draw.assert_called()

if __name__ == "__main__":
    unittest.main()
