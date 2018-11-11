import sys
import pygame
from src.Ball import *
from src.Platform import *
from src.Plate import *
from settings import *
import random


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
            speed[0] = -speed[0]-1
        else:
            speed[0] = -speed[0]+1

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

pygame.init()

screen = pygame.display.set_mode(size)
ball_speed = [0, -1]
ball = Ball((500, 449))

platform = Platform((450, 470))
plate = Plate ((500, 100))
myball = Ball((30, 30))

plates = []
y_row = 5
for row in range (3):
    x_row = 5
    for column in range (16):
        plates.append(Plate((x_row, y_row)))
        x_row +=55
    y_row += 25


running = True
game_started = False
game_over = False

game_objects = {
    'ball' : ball,
    'platform' : platform,
    'plates' : plates
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_started:
                    game_started = True
                else:
                    game_started = False

    if game_started:
        #If space pressed the real game starts
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            platform.move(-2)
        elif keys[pygame.K_RIGHT]:
            platform.move(2)

        myball.move(speed)
        change_speed(myball, speed)
        if not change_speed(ball, ball_speed):
            game_over = True

        if destroy_collisioned(ball, game_objects['plates']):
            change_speed(ball, ball_speed, True)

        if platform.colliderect(ball.get_rect()):
            change_speed(ball, ball_speed, True)

        if game_started:
            ball.move(ball_speed)

    screen.fill(black)

    if game_over:
        show_game_over(screen)

    draw_objects(screen, game_objects)
    myball.draw(screen)

    pygame.display.flip()