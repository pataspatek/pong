import pygame
from background import SCREEN_HEIGHT, SCREEN_WIDTH

PADDLE_HEIGHT = 100
PADDLE_WIDTH = 10

GAP = 30

COLOR = "white"

class Paddle:


    def __init__(self, surface):
        self.surface = surface
        self.player_rect = pygame.Rect(GAP, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.opponent_rect = pygame.Rect(SCREEN_WIDTH - GAP - PADDLE_WIDTH, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

 
    def paddle_create(self, rect):
        pygame.draw.rect(self.surface, COLOR, rect)


    def paddle_move(self, key_press):

        if key_press[pygame.K_w] and self.player_rect.y > 0:
            self.player_rect.y -= 10
        elif key_press[pygame.K_s] and self.player_rect.y < SCREEN_HEIGHT - self.player_rect.height:
            self.player_rect.y += 10

        if key_press[pygame.K_UP] and self.opponent_rect.y > 0:
            self.opponent_rect.y -= 10
        elif key_press[pygame.K_DOWN] and self.opponent_rect.y < SCREEN_HEIGHT - self.opponent_rect.height:
            self.opponent_rect.y += 10

    

        



