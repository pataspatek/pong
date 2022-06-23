import pygame
import random
from background import SCREEN_HEIGHT, SCREEN_WIDTH

BALL_RADIUS = 15

COLOR = "white"

class Ball:

    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(SCREEN_WIDTH / 2 - BALL_RADIUS / 2, SCREEN_HEIGHT / 2 - BALL_RADIUS / 2, BALL_RADIUS, BALL_RADIUS)
        self.ball_generate_speed()
    

    def ball_create(self):
        pygame.draw.ellipse(self.surface, COLOR, self.rect)


    def ball_starting_position(self):
        self.rect.x = SCREEN_WIDTH / 2 - self.rect.width / 2
        self.rect.y = SCREEN_HEIGHT / 2 - self.rect.height / 2


    def ball_generate_speed(self):
        numbers = [-10, -9, -8, -7, -6, -5, 5, 6, 7, 8, 9, 10]
        x = random.choice(numbers)
        y = random.choice(numbers)
        self.speed = [x , y]
        

    def ball_move(self):
        self.rect.x -= self.speed[0]
        self.rect.y -= self.speed[1]

        if self.rect.x < 0 or self.rect.x + self.rect.width > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]

        if self.rect.y < 0 or self.rect.y + self.rect.height > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
