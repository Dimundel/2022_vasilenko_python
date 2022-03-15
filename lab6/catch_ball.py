import pygame
from random import randint

pygame.init()

FPS = 30
DT = 1
screen = pygame.display.set_mode((1200, 900))
FONT = pygame.font.SysFont("Arial", 40)
NUMBER_OF_BALLS = 20

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def create_object(object_type):
    """
    draws new object
    """
    x = randint(200, 1000)
    y = randint(200, 800)
    r = randint(10, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]

    if object_type == "ball":
        pygame.draw.circle(screen, color, (x, y), r)

    if object_type == "square":
        pygame.draw.rect(screen, color, (x - r, y - r, 2 * r, 2 * r))

    new_object = [x, y, r, vx, vy, color, ]
    return new_object


def move_object(the_object):
    """
    moves balls
    """
    the_object[0] += the_object[3] * DT
    the_object[1] += the_object[4] * DT
    if the_object[0] <= the_object[2] or the_object[0] >= 1200 - the_object[2]:
        the_object[3] = -the_object[3]
    if the_object[1] <= the_object[2] or the_object[1] >= 900 - the_object[2]:
        the_object[4] = -the_object[4]
    pygame.draw.circle(screen, the_object[5], (the_object[0], the_object[1]), the_object[2])


score = 0
balls = []
squares = []

clock = pygame.time.Clock()
finished = False

for i in range(NUMBER_OF_BALLS):
    balls.append(create_object("ball"))

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
                    balls[balls.index(ball)] = create_object("ball")

    for ball in balls:
        move_object(ball)

    score_surface = FONT.render("Score: {}".format(score), False, (255, 255, 255))
    screen.blit(score_surface, (0, 0))
    pygame.display.update()

pygame.quit()
