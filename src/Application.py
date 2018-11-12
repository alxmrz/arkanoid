import sys
import pygame
from src.Ball import *
from src.Platform import *
from src.Plate import *
from src.functions import *
from settings import *


class Application:

    def __init__(self):
        self.running = True
        self.game_started = False
        self.game_over = False
        self.game_objects = {
            'ball': None,
            'platform': None,
            'plates': []
        }

    def run(self):
        self.init_window()
        self.init_game_objects()
        while self.running:
            self.handle_events()
            if self.game_started:
                self.handle_platform_moving()
                if not self.change_speed():
                    self.game_over = True

                if self.destroy_collisioned():
                    self.change_speed_collisioned()

                if self.platform.colliderect(self.ball.get_rect()):
                    self.change_speed_collisioned()

                self.ball.move()

            self.display_scene()

    def init_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arkanoid")

    def create_plates_table(self):
        result = []
        y_row = 5
        for row in range(3):
            x_row = 5
            for column in range(16):
                result.append(Plate((x_row, y_row)))
                x_row += 55
            y_row += 25

        return result

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_started:
                        self.game_started = True
                    elif self.game_over:
                        self.game_over = False
                        self.init_game_objects()
                    else:
                        self.game_started = False

    def handle_platform_moving(self):
        # If space pressed the real game starts
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.platform.move(-2)
        elif keys[pygame.K_RIGHT]:
            self.platform.move(2)

    def display_scene(self):
        self.screen.fill(black)

        if self.game_over:
            self.show_text('Game over', (500, 300))
            self.show_text('Press [space] to start new game', (500, 450))
        if not self.game_started:
            self.show_text('Press [space] to start new game', (500, 300))
        self.draw_objects()

        pygame.display.flip()

    def init_game_objects(self):
        self.ball = Ball((500, 449))
        self.platform = Platform((450, 470))
        self.plates = self.create_plates_table()

        self.game_objects = {
            'ball': self.ball,
            'platform': self.platform,
            'plates': self.plates
        }

    def change_speed(self):
        if self.ball.x < 0 or self.ball.x > width:
            self.ball.speed[0] = -self.ball.speed[0]
        if self.ball.y < 0:
            self.ball.speed[1] = -self.ball.speed[1]
        if self.ball.y > height:
            return False

        return True

    def change_speed_collisioned(self):
        rand = random.randint(1, 3)
        if rand % 2 == 0:
            self.ball.speed[0] = -self.ball.speed[0] - 1
        else:
            self.ball.speed[0] = -self.ball.speed[0] + 1

        if abs(self.ball.speed[0]) >= 1:
            self.ball.speed[0] = 1
            self.ball.speed[1] = -self.ball.speed[1]

    def draw_objects(self):
        for name, object in self.game_objects.items():
            if name == 'plates':
                for plate in object:
                    plate.draw(self.screen)
            else:
                object.draw(self.screen)

    def destroy_collisioned(self):
        for index, object in enumerate(self.plates):
            if object.colliderect(self.ball.get_rect()):
                del self.plates[index]
                return True

        return False

    def show_text(self, text, coords):
        myfont = pygame.font.SysFont('freesansbold.ttf', 50)
        textsurface = myfont.render(text, True, (255, 255, 255))
        textsurfaceRectObj = textsurface.get_rect()
        textsurfaceRectObj.center = coords
        self.screen.blit(textsurface, textsurfaceRectObj)