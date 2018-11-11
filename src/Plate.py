import pygame


class Plate(pygame.Rect):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        super().__init__((self.x, self.y), (50, 10))

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y, 50, 10])