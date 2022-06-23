import pygame
from ball import Ball
from paddle import Paddle
from background import Background, SCREEN_HEIGHT, SCREEN_WIDTH
from scoreboard import Scoreboard
pygame.init()


DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = Background(DISPLAY)
scoreboard = Scoreboard(DISPLAY)
ball = Ball(DISPLAY)
paddle = Paddle(DISPLAY)


def draw_screen(player, opponent):
    background.background_draw()
    background.border_draw()
    scoreboard.score_write()

    ball.ball_create()
    paddle.paddle_create(player)
    paddle.paddle_create(opponent)


def main ():
    clock = pygame.time.Clock()

    ballrect = ball.rect
    player = paddle.player_rect
    opponent = paddle.opponent_rect
    
    start = False
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_SPACE]:
            start = True
        if start:
            ball.ball_move()

        paddle.paddle_move(key_press)


        if ballrect.colliderect(player) or ballrect.colliderect(opponent):
            ball.speed[0] *= -1


        if ballrect.x < 0:
            scoreboard.opponent_score += 1
            start = False
            ball.ball_starting_position()
            ball.ball_generate_speed()

        if ballrect.x + ballrect.width > SCREEN_WIDTH:
            scoreboard.player_score += 1
            start = False
            ball.ball_starting_position()
            ball.ball_generate_speed()


        draw_screen(player, opponent)

        clock.tick(60)
        pygame.display.update()

    main()


if __name__ == "__main__":
    main()