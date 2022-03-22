import pygame
from random import randint

user = input("Enter your username: ")

pygame.init()

FPS = 30
DT = 1
FONT = pygame.font.SysFont("Arial", 40)
NUMBER_OF_CIRCLES = 10
NUMBER_OF_SQUARES = 10
SCREEN_SIZE = (1200, 900)
time = 10

screen = pygame.display.set_mode(SCREEN_SIZE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def write_score(file, username, users_score):
    """
    writes score to a file
    :param file: file where score is safed
    :param username: name of user
    :param users_score: user's score
    """
    was_username = False
    f = open(file, "r")
    datas = f.readlines()
    print(datas)
    f.close()
    f = open(file, "w")

    for data in datas:

        if data.split(": ")[0] == username:
            was_username = True

            if int(data.split(": ")[1]) < users_score:
                f.write(username + ": " + str(users_score) + "\n")
            else:
                f.write(data)

        else:
            f.write(data)

    if not was_username:
        f.write(username + ": " + str(users_score) + "\n")

    f.close()


def create_object(object_type):
    """
    draws new object of certain type
    :param object_type: circle or square
    :return: list of objects parameters
    """
    x = randint(200, 1000)
    y = randint(200, 800)
    r = randint(10, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]

    if object_type == "circle":
        pygame.draw.circle(screen, color, (x, y), r)

    if object_type == "square":
        pygame.draw.rect(screen, color, (x - r, y - r, 2 * r, 2 * r))

    new_object = [x, y, r, vx, vy, color, object_type]
    return new_object


def move_object(the_object):
    """
    move object for the DT time
    :param the_object: object that will move
    """
    the_object[0] += the_object[3] * DT
    the_object[1] += the_object[4] * DT

    if the_object[6] == "circle":
        pygame.draw.circle(screen, the_object[5], (the_object[0], the_object[1]), the_object[2])
        if the_object[0] <= the_object[2] or the_object[0] >= SCREEN_SIZE[0] - the_object[2]:
            the_object[3] = -the_object[3]
        if the_object[1] <= the_object[2] or the_object[1] >= SCREEN_SIZE[1] - the_object[2]:
            the_object[4] = -the_object[4]

    if the_object[6] == "square":
        pygame.draw.rect(screen, the_object[5],
                         (the_object[0] - the_object[2], the_object[1] - the_object[2], 2 * the_object[2],
                          2 * the_object[2]))
        if the_object[0] <= the_object[2] or the_object[0] >= SCREEN_SIZE[0] - the_object[2] or \
                the_object[1] <= the_object[2] or the_object[1] >= SCREEN_SIZE[1] - the_object[2]:
            the_object[3] = -the_object[3]
            the_object[4] = -the_object[4]
            the_object[5] = COLORS[randint(0, 5)]


score = 0
circles = []
squares = []

clock = pygame.time.Clock()
finished = False

for i in range(NUMBER_OF_CIRCLES):
    circles.append(create_object("circle"))

for j in range(NUMBER_OF_SQUARES):
    squares.append(create_object("square"))

while not finished:
    screen.fill(BLACK)
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:

            for circle in circles:

                if (pygame.mouse.get_pos()[0] - circle[0]) ** 2 + (pygame.mouse.get_pos()[1] - circle[1]) ** 2 <= \
                        circle[2] ** 2:
                    score += 1
                    circles[circles.index(circle)] = create_object("circle")

            for square in squares:

                if abs(pygame.mouse.get_pos()[0] - square[0]) <= square[2] and abs(
                        pygame.mouse.get_pos()[1] - square[1]) <= square[2]:
                    score += 3
                    squares[squares.index(square)] = create_object("square")

    for circle in circles:
        move_object(circle)
    for square in squares:
        move_object(square)

    score_surface = FONT.render("Score: {}".format(score), False, (255, 255, 255))
    screen.blit(score_surface, (0, 0))
    time -= 1 / FPS
    ui_surface = FONT.render("Time: {}".format(int(time)), False, (255, 255, 255))
    screen.blit(ui_surface, (SCREEN_SIZE[0] - 140, 0))
    pygame.display.update()

    if time <= 0:
        finished = True

pygame.quit()

write_score("score.txt", user, score)
