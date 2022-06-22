import pygame
from background import BACKGROUND, BORDER_WIDTH, SCREEN_WIDTH


SCOREBOARD_HEIGHT = 80
SCOREBOARD_WIDTH = (1 / 2) * SCOREBOARD_HEIGHT

DISTANCE_FROM_WALL = 15

COLOR = "white"
FONT = "arial"

class Scoreboard():

    def __init__(self, surface, number):
        self.surface = surface
        self.number = number
        self.score = 0


    def score_write(self):
        if self.number == 1:
            x = SCREEN_WIDTH / 2 - SCOREBOARD_WIDTH - BORDER_WIDTH / 2 - DISTANCE_FROM_WALL
        else:
            x = SCREEN_WIDTH / 2 + BORDER_WIDTH / 2 + DISTANCE_FROM_WALL
        
        SCOREBOARD = pygame.draw.rect(self.surface, BACKGROUND, pygame.Rect(x, 0, SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT))

        font = pygame.font.SysFont(FONT, SCOREBOARD_HEIGHT)
        text = font.render(f"{self.score}", False,  COLOR)
        self.surface.blit(text, (SCOREBOARD))

    def score_increase(self):
        self.score += 1

