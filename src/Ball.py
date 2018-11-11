import pygame


class Ball:

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def move(self, coords):
        self.x += coords[0]
        self.y += coords[1]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 20)
