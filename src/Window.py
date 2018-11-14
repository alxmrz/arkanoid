from src.UI import *
import pygame


class Window():

    def __init__(self, app, width, height, title):
        self.title = title
        self.width = width
        self.height = height
        self.UI = UI(app)
        self.app = app
        self.screen = None

    def init(self):
        """
        Init window and screen painter
        :return: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def display(self):
        """
        Display the game, including UI
        :return: None
        """
        self.screen.fill(self.app.colors['black'])

        self._draw_scene_objects()
        self.UI.show()

        pygame.display.flip()

    def _draw_scene_objects(self):
        """
        Draw game objects for interaction
        :return: None
        """
        for name, object in self.app.game_objects.items():
            if name == 'plates':
                for plate in object:
                    plate.draw(self.screen)
            else:
                object.draw(self.screen)
