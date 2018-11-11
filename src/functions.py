import pygame
import random
from settings import *


def change_speed(ball, speed, collisioned = False):
    if not collisioned:
        if ball.x < 0 or ball.x > width:
            speed[0] = -speed[0]
        if ball.y < 0:
            speed[1] = -speed[1]
        if ball.y > height:
            return False
    else:
        rand = random.randint(1,3)
        if rand % 2 == 0:
            speed[0] = -speed[0] -1
        else:
            speed[0] = -speed[0] + 1

        if abs(speed[0]) > 3:
            speed[0] = 1
        speed[1] = -speed[1]

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
            print ('destroy')
            del objects[index]
            return True

    return False

def show_game_over(screen):
    myfont = pygame.font.SysFont('freesansbold.ttf', 50)
    textsurface = myfont.render('Game over', True, (255, 255, 255))
    textsurfaceRectObj = textsurface.get_rect()
    textsurfaceRectObj.center = (500, 300)
    screen.blit(textsurface, textsurfaceRectObj)
