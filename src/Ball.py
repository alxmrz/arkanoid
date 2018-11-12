import pygame


class Ball(pygame.Rect):

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.speed = [0, -1]
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
