import pygame
from ball import Ball
from player import Player
from background import Background, SCREEN_HEIGHT, SCREEN_WIDTH
from scoreboard import Scoreboard
pygame.init()


DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = Background(DISPLAY)
player_one = Player(DISPLAY, 1)
player_two = Player(DISPLAY, 2)
ball = Ball(DISPLAY)
score_one = Scoreboard(DISPLAY, 1)
score_two = Scoreboard(DISPLAY, 2)

def draw_screen():
    background.background_draw()
    background.border_draw()
    score_one.score_write()
    score_two.score_write()
    player_one.platform_draw()
    player_two.platform_draw()
    ball.ball_create()

def main ():
    clock = pygame.time.Clock()

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        player_one.platform_move()
        player_two.platform_move()
        draw_screen()

        clock.tick(60)
        pygame.display.update()

    main()


if __name__ == "__main__":
    main()