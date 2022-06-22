import pygame
from background import SCREEN_HEIGHT, SCREEN_WIDTH


COLOR = "white" # Variable that changes the color of the player platforms. 

BALL_RADIUS = 10


class Ball:


    def __init__(self, surface):
        self.surface = surface
        self.centerx = SCREEN_WIDTH / 2
        self.centery = SCREEN_HEIGHT / 2
        self.left = self.centerx - BALL_RADIUS / 2
        self.right = self.centerx + BALL_RADIUS / 2
        self.up = self.centery - BALL_RADIUS / 2
        self.up = self.centery + BALL_RADIUS / 2



    def ball_create(self):
        pygame.draw.circle(self.surface, COLOR, (self.centerx, self.centery), BALL_RADIUS)


    def ball_move(self):
        pass


    # def ball_start(self):
    #     key_press = pygame.key.get_pressed()

    #     if key_press[pygame.K_w] and self.y > 0:
    #         self.y -= 10
