import pygame
from background import BACKGROUND, BORDER_WIDTH, SCREEN_WIDTH

SCOREBOARD_HEIGHT = 80
SCOREBOARD_WIDTH = (1 / 2) * SCOREBOARD_HEIGHT

DISTANCE_FROM_WALL = 15

COLOR = "white"
FONT = "arial"

class Scoreboard():


    def __init__(self, surface):
        self.surface = surface
        self.player_score = 0
        self.opponent_score = 0
        

    def score_write(self):
        player = pygame.draw.rect(self.surface, BACKGROUND, pygame.Rect(SCREEN_WIDTH / 2 - SCOREBOARD_WIDTH - BORDER_WIDTH / 2 - DISTANCE_FROM_WALL, 0, SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT))
        opponent = pygame.draw.rect(self.surface, BACKGROUND, pygame.Rect(SCREEN_WIDTH / 2 + BORDER_WIDTH / 2 + DISTANCE_FROM_WALL, 0, SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT))

        font = pygame.font.SysFont(FONT, SCOREBOARD_HEIGHT)
        player_text = font.render(f"{self.player_score}", False,  COLOR)
        opponent_text = font.render(f"{self.opponent_score}", False,  COLOR)

        self.surface.blit(player_text, player)
        self.surface.blit(opponent_text, opponent)


    def score_increase(self):
        self.score += 1

