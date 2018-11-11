import sys
import pygame
from src.Ball import *
from src.Platform import *
from settings import *


pygame.init()

screen = pygame.display.set_mode(size)

ball = Ball((500, 450))
platform = Platform((450, 470))

myball = Ball((10, 10))
myball1 = Ball((20, 10))
myball2 = Ball((30, 10))
myball3 = Ball((40, 10))

print(sys.getfilesystemencoding())
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                platform.move(-3)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform.move(-2)
    elif keys[pygame.K_RIGHT]:
        platform.move(2)

    myball.move(speed)
    if myball.x < 0 or myball.x > width:
        speed[0] = -speed[0]
    if myball.y < 0 or myball.y > height:
        speed[1] = -speed[1]

    screen.fill(black)
    #pygame.draw.rect(screen, (255, 255, 255), ballrect)
    myball.draw(screen)
    ball.draw(screen)
    platform.draw(screen)
    #screen.blit(ball, ballrect)
    pygame.display.flip()