import pygame
from random import randint

pygame.init()

FPS = 30
DT = 1
screen = pygame.display.set_mode((1200, 900))
FONT = pygame.font.SysFont("Arial", 40)
NUMBER_OF_BALLS = 10

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """
    draws new ball
    """
    x = randint(200, 1000)
    y = randint(200, 800)
    r = randint(10, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    pygame.draw.circle(screen, color, (x, y), r)
    ball = [x, y, r, vx, vy, color]
    return ball


def move_ball(ball):
    """
    moves ball
    """
    ball[0] += ball[3] * DT
    ball[1] += ball[4] * DT
    if ball[0] <= ball[2] or ball[0] >= 1200 - ball[2]:
        ball[3] = -ball[3]
    if ball[1] <= ball[2] or ball[1] >= 900 - ball[2]:
        ball[4] = -ball[4]
    pygame.draw.circle(screen, ball[5], (ball[0], ball[1]), ball[2])
    return ball


score = 0
balls = []

clock = pygame.time.Clock()
finished = False

for i in range(NUMBER_OF_BALLS):
    balls.append(new_ball())

while not finished:
    screen.fill(BLACK)
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:

            for ball in balls:

                if (pygame.mouse.get_pos()[0] - ball[0]) ** 2 + (pygame.mouse.get_pos()[1] - ball[1]) ** 2 <= \
                        ball[2] ** 2:
                    score += 1
                    balls[balls.index(ball)] = new_ball()

    for ball in balls:
        ball = move_ball(ball)

    score_surface = FONT.render("Score: {}".format(score), False, (255, 255, 255))
    screen.blit(score_surface, (0, 0))
    pygame.display.update()

pygame.quit()
