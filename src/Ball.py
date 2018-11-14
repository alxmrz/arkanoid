import pygame
import random
from src.Window import *

class Ball():

    def __init__(self, app, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.speed = [0, -1]
        self.app = app
        self.rect = pygame.Rect((self.x-20, self.y-20), (40, 40))

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.x = self.x - 20
        self.rect.y = self.y - 20

    def get_rect(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 20)

    def change_direction_border(self):
        """
        Change ball direction if its on the screen and collided borders
        """
        if self.x < 0 or self.x > self.app.window.width:
            self.speed[0] = -self.speed[0]
        if self.y < 0:
            self.speed[1] = -self.speed[1]

    def change_direction_plate(self):
        """
        Change speed of a ball when a plate is collided
        :return: None
        """
        self.speed[0] = random.randint(-1, 1) * 2
        self.speed[1] = random.randint(-1, 1) * 2

        if self.speed[0] == 0:
            self.speed[0] = 1
        elif self.speed[1] == 0:
            self.speed[1] = 1

    def change_direction_platform(self):
        """
        Change speed of a ball when platform is collided
        :return: None
        """
        if self.x <= self.app.platform.x + 25:
            self.speed = [-2, -1]
        elif self.x <= self.app.platform.x + 50:
            self.speed = [-1, -1]
        elif self.x <= self.app.platform.x + 75:
            self.speed = [1, -1]
        elif self.x <= self.app.platform.x + 100:
            self.speed = [2, -1]
