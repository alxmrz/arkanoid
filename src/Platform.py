import pygame


class Platform(pygame.Rect):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        super().__init__((self.x, self.y), (100, 10))

    def move(self, x):
        self.x +=x

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, 50, 10])
        pygame.draw.rect(screen, (0, 0, 255), [self.x+50, self.y, 50, 10])
