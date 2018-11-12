import pygame
import random
from settings import *


def change_speed(ball, collisioned = False):
    if not collisioned:
        if ball.x < 0 or ball.x > width:
            ball.speed[0] = -ball.speed[0]
        if ball.y < 0:
            ball.speed[1] = -ball.speed[1]
        if ball.y > height:
            return False
    else:
        rand = random.randint(1,3)
        if rand % 2 == 0:
            ball.speed[0] = -ball.speed[0] -1
        else:
            ball.speed[0] = -ball.speed[0] + 1

        if abs(ball.speed[0]) >= 1:
            ball.speed[0] = 1
            ball.speed[1] = -ball.speed[1]

    return True

def draw_objects(screen, game_objects):
    for name, object in game_objects.items():
        if name == 'plates':
            for plate in object:
                plate.draw(screen)
        else:
            object.draw(screen)

def destroy_collisioned(ball, objects):
    for index, object in enumerate(objects):
        if object.colliderect(ball.get_rect()):
            del objects[index]
            return True

    return False

def show_game_over(screen):
    myfont = pygame.font.SysFont('freesansbold.ttf', 50)
    textsurface = myfont.render('Game over', True, (255, 255, 255))
    textsurfaceRectObj = textsurface.get_rect()
    textsurfaceRectObj.center = (500, 300)
    screen.blit(textsurface, textsurfaceRectObj)
