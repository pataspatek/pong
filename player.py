import pygame
from background import SCREEN_HEIGHT, SCREEN_WIDTH


COLOR = "white" # Variable that changes the color of the player platforms. 

PLATFORM_HEIGHT = 70
PLATFORM_WIDTH = 10

DISTANCE_FROM_WALL = 30

class Player:


    def __init__(self, surface, number):
        self.surface = surface
        self.number = number
        self.y = SCREEN_HEIGHT / 2 - PLATFORM_HEIGHT / 2
        if self.number == 1:
            self.x = DISTANCE_FROM_WALL
        else:
            self.x = SCREEN_WIDTH - DISTANCE_FROM_WALL - PLATFORM_WIDTH

    def platform_draw(self):
        pygame.draw.rect(self.surface, COLOR, pygame.Rect(self.x, self.y, PLATFORM_WIDTH, PLATFORM_HEIGHT))


    def platform_move(self):
        key_press = pygame.key.get_pressed()

        if self.number == 1:
            if key_press[pygame.K_w] and self.y > 0:
                self.y -= 10
            elif key_press[pygame.K_s] and self.y < SCREEN_HEIGHT - PLATFORM_HEIGHT:
                self.y += 10

        else:
            if key_press[pygame.K_UP] and self.y > 0:
                self.y -= 10
            elif key_press[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - PLATFORM_HEIGHT:
                self.y += 10