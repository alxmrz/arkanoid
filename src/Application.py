import sys
import random
import pygame
from src.Ball import *
from src.Platform import *
from src.Plate import *
from settings import *


class Application:

    def __init__(self):
        self.running = True
        self.game_started = False
        self.game_over = False
        self.score = 0
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
        self.init_window()
        self.init_game_objects()

        while self.running:
            self.handle_events()
            if self.game_started and not self.game_over:
                self.handle_platform_moving()
                if not self.change_speed():
                    self.game_over = True

                if self.destroy_collided():
                    self.change_speed_collided()

                if self.platform.colliderect(self.ball.get_rect()):
                    self.change_speed_platform()

                self.ball.move()

            self.display_scene()

    def init_window(self):
        """
        Init window and screen painter
        :return: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Arkanoid")

    def create_plates_table(self):
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

    def handle_events(self):
        """
        Handling events
        :return: None
        """
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
        """
        Change platform position when pressed arrows keys
        :return:
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.platform.x - 1 >= 0:
            self.platform.move(-4)
        elif keys[pygame.K_RIGHT] and self.platform.x + 101 <= width:
            self.platform.move(4)

    def display_scene(self):
        """
        Display the game, including UI
        :return: None
        """
        self.screen.fill(black)

        if self.game_over:
            self.show_text('Game over!', (500, 300))
            self.show_text('Your score: ' + str(self.score), (500, 400))
            self.show_text('Press [space] to start new game', (500, 450))
        elif not self.game_started:
            self.show_text('Press [space] to start new game', (500, 300))
        elif not self.game_objects['plates']:
            self.game_over = True
            self.show_text('You win!', (500, 300))
            self.show_text('Your score: ' + str(self.score), (500, 400))
            self.show_text('Press [space] to start new game', (500, 450))
        else:
            self.show_text('Score: ' + str(self.score), (100, 550))

        self.draw_objects()

        pygame.display.flip()

    def init_game_objects(self):
        """
        Init start game state
        :return: None
        """
        self.ball = Ball((500, 449))
        self.platform = Platform((450, 590))
        self.plates = self.create_plates_table()
        self.score = 0

        self.game_objects = {
            'ball': self.ball,
            'platform': self.platform,
            'plates': self.plates
        }

    def change_speed(self):
        """
        Change ball speed if its on the screen
        If not return False
        :return: bool
        """
        if self.ball.x < 0 or self.ball.x > width:
            self.ball.speed[0] = -self.ball.speed[0]
        if self.ball.y < 0:
            self.ball.speed[1] = -self.ball.speed[1]
        if self.ball.y > height:
            return False

        return True

    def change_speed_collided(self):
        """
        Change speed of a ball when a plate is destroyed
        :return: None
        """
        self.ball.speed[0] = random.randint(-1, 1) * 2
        self.ball.speed[1] = random.randint(-1, 1) * 2

        if self.ball.speed[0] == 0:
            self.ball.speed[0] = 1
        elif self.ball.speed[1] == 0:
            self.ball.speed[1] = 1

    def change_speed_platform(self):
        """
        Change speed of a ball when platform is collided
        :return: None
        """
        if self.ball.x <= self.platform.x + 25:
            self.ball.speed = [-2, -1]
        elif self.ball.x <= self.platform.x + 50:
            self.ball.speed = [-1, -1]
        elif self.ball.x <= self.platform.x + 75:
            self.ball.speed = [1, -1]
        elif self.ball.x <= self.platform.x + 100:
            self.ball.speed = [2, -1]

    def draw_objects(self):
        """
        Draw game objects for interaction
        :return: None
        """
        for name, object in self.game_objects.items():
            if name == 'plates':
                for plate in object:
                    plate.draw(self.screen)
            else:
                object.draw(self.screen)

    def destroy_collided(self):
        """
        Destroy collided object and increment score
        If non object can be destroyed return False
        :return: bool
        """
        for index, object in enumerate(self.plates):
            if object.colliderect(self.ball.get_rect()):
                del self.plates[index]
                self.score += 10
                return True

        return False

    def show_text(self, text, coords):
        """
        Show text on the screen
        :param text: string
        :param coords: list
        :return: None
        """
        myfont = pygame.font.SysFont('freesansbold.ttf', 50)
        textsurface = myfont.render(text, True, (255, 255, 255))
        textsurfaceRectObj = textsurface.get_rect()
        textsurfaceRectObj.center = coords
        self.screen.blit(textsurface, textsurfaceRectObj)