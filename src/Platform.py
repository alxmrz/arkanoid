from settings import black
import pygame


class Platform:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def move(self, x):
        self.x +=x

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y, 100, 10])
