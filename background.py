import pygame

SCREEN_WIDTH = 1000 
SCREEN_HEIGHT = 800

BORDER_WIDTH = 3
BORDER_HEIGHT = 40
SPACE_HEIGHT = BORDER_HEIGHT / 8

BACKGROUND = "black" #Change the color of the background.
BORDER = "white" #Change the color of border in middle of the screen.


class Background:


    def __init__(self, surface):
        self.surface = surface


    def background_draw(self):
        self.surface.fill(BACKGROUND)


    def border_draw(self):
        y = 0
        for i in range(int(SCREEN_HEIGHT / (BORDER_HEIGHT + SPACE_HEIGHT * 2))):
            pygame.draw.rect(self.surface, BACKGROUND, pygame.Rect(SCREEN_WIDTH / 2 - BORDER_WIDTH / 2, y, BORDER_WIDTH, SPACE_HEIGHT))
            y += SPACE_HEIGHT
            pygame.draw.rect(self.surface, BORDER, pygame.Rect(SCREEN_WIDTH / 2 - BORDER_WIDTH / 2, y, BORDER_WIDTH, BORDER_HEIGHT))
            y += BORDER_HEIGHT
            pygame.draw.rect(self.surface, BACKGROUND, pygame.Rect(SCREEN_WIDTH / 2 - BORDER_WIDTH / 2, y, BORDER_WIDTH, SPACE_HEIGHT))
            y += SPACE_HEIGHT
