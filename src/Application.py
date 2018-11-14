import sys
import pygame
from src.Ball import *
from src.Platform import *
from src.Plate import *
from src.Window import *


class Application:
    def __init__(self):
        self.running = True
        self.game_started = False
        self.game_over = False
        self.score = 0
        self.window = Window(self, 900, 600, 'Arkanoid')
        self.game_objects = {
            'ball': None,
            'platform': None,
            'plates': []
        }

    def run(self):
        """
        Main function of the game
        :return: None
        """
        self.window.init()
        self._init_game_objects()

        while self.running:
            self._handle_events()
            if self.game_started and not self.game_over:
                self._handle_platform_moving()

                self.ball.change_direction_border()

                if self._destroy_collided_plates():
                    self.ball.change_direction_plate()

                if self.platform.colliderect(self.ball.get_rect()):
                    self.ball.change_direction_platform()

                self.ball.move()

                # if self.ball is outside the screen game is over
                self.game_over = self.ball.y > self.window.height

            self.window.display()

    def _create_plates_table(self):
        """
        Creates plates table for destroying. 9 row and 16 columns.
        :return:
        """
        result = []
        y_row = 5
        for row in range(9):
            x_row = 5
            for column in range(16):
                result.append(Plate((x_row, y_row)))
                x_row += 55
            y_row += 25

        return result

    def _handle_events(self):
        """
        Handling events
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_started:
                        self.game_started = True
                    elif self.game_over:
                        self.game_over = False
                        self._init_game_objects()
                    else:
                        self.game_started = False

    def _handle_platform_moving(self):
        """
        Change platform position when pressed arrows keys
        :return:
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.platform.x - 1 >= 0:
            self.platform.move(-4)
        elif keys[pygame.K_RIGHT] and self.platform.x + 101 <= self.window.width:
            self.platform.move(4)

    def _init_game_objects(self):
        """
        Init primary game state
        :return: None
        """
        self.ball = Ball(self, (500, 449))
        self.platform = Platform((450, 590))
        self.plates = self._create_plates_table()
        self.score = 0

        self.game_objects = {
            'ball': self.ball,
            'platform': self.platform,
            'plates': self.plates
        }

    def _destroy_collided_plates(self):
        """
        Destroy collided object and increment score
        If no one object can be destroyed return False
        :return: bool
        """
        for index, object in enumerate(self.plates):
            if object.colliderect(self.ball.get_rect()):
                del self.plates[index]
                self.score += 10
                return True

        return False

