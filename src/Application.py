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
            'plates': None
        }

    def run(self):
        self.init_window()
        self.init_game_objects()
        while self.running:
            self.handle_events()
            if self.game_started:
                self.handle_platform_moving(self.game_objects['platform'])
                if not change_speed(self.game_objects['ball']):
                    self.game_over = True

                if destroy_collisioned(self.game_objects['ball'], self.game_objects['plates']):
                    change_speed(self.game_objects['ball'], True)

                if self.game_objects['platform'].colliderect(self.game_objects['ball'].get_rect()):
                    change_speed(self.game_objects['ball'], True)

                self.game_objects['ball'].move()

            self.display_scene(self.game_objects)

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

    def handle_platform_moving(self, platform):
        # If space pressed the real game starts
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            platform.move(-2)
        elif keys[pygame.K_RIGHT]:
            platform.move(2)

    def display_scene(self, game_objects):
        self.screen.fill(black)

        if self.game_over:
            show_game_over(self.screen)
        draw_objects(self.screen, game_objects)

        pygame.display.flip()

    def init_game_objects(self):
        ball = Ball((500, 449))

        platform = Platform((450, 470))

        plates = self.create_plates_table()

        self.game_objects = {
            'ball': ball,
            'platform': platform,
            'plates': plates
        }
