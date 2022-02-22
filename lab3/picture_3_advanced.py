import pygame

pygame.init()

FPS = 30
WINDOW_SIZE = (1200, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
COLORS = {'BLACK': (0, 0, 0), 'GREY': (167, 141, 179), 'PINK': (239, 61, 255),
          'RED': (255, 5, 55), 'ORANGE': (235, 152, 59), 'CHOCOLATE': (112, 87, 59),
          'CRIMSON': (255, 61, 87), 'FLASH': (237, 204, 161), 'SNOW_COLOR': (212, 252, 255),
          'BLUE': (100, 0, 255)
          }


def make_girl(size, cord, flip):
    """
    param
    :param size: How much to compress a 2D drawing
    :param cord: drawing creation coordinates
    :param flip: drawing creation coordinates
    :return: painted girl
    """
    surface_girl = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
    pygame.draw.polygon(surface_girl, COLORS['PINK'], ((800, 250), (700, 550), (900, 550)))
    pygame.draw.line(surface_girl, COLORS['BLACK'], (800, 250), (700, 550))
    pygame.draw.line(surface_girl, COLORS['BLACK'], (700, 550), (900, 550))
    pygame.draw.line(surface_girl, COLORS['BLACK'], (800, 250), (900, 550))
    pygame.draw.circle(surface_girl, COLORS['FLASH'], (800, 220), 60)
    pygame.draw.circle(surface_girl, COLORS['BLACK'], (800, 220), 60, 2)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (850, 170), (820, 190), 2)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (750, 160), (780, 180), 2)
    pygame.draw.circle(surface_girl, COLORS['RED'], (800, 220), 10)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (950, 300), (900, 360), 3)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (820, 340), (900, 360), 3)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (780, 340), (600, 410), 3)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (750, 550), (750, 700), 3)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (700, 700), (750, 700), 3)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (820, 550), (820, 700), 3)
    pygame.draw.line(surface_girl, COLORS['BLACK'], (820, 700), (870, 700), 3)
    surface_girl = pygame.transform.scale(surface_girl, size)
    surface_girl = pygame.transform.flip(surface_girl, flip, False)
    screen.blit(surface_girl, cord)


def make_dude(size, cord, flip):
    """
    param
    :param size: How much to compress a 2D drawing
    :param cord: drawing creation coordinates
    :param flip: drawing creation coordinates
    :return: painted dude
    """
    surface_dude = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
    pygame.draw.ellipse(surface_dude, COLORS['GREY'], (300, 250, 150, 300))
    pygame.draw.ellipse(surface_dude, COLORS['BLACK'], (300, 250, 150, 300), 1)
    pygame.draw.circle(surface_dude, COLORS['FLASH'], (375, 200), 70)
    pygame.draw.circle(surface_dude, COLORS['BLACK'], (375, 200), 70, 2)
    pygame.draw.line(surface_dude, COLORS['BLACK'], (60+375-10, 200-10), (60+375-40, 200-40), 3)
    pygame.draw.line(surface_dude, COLORS['BLACK'], (-40+375+10, 200+10-50), (-40+375+40-60, 200+40-50), 3)
    pygame.draw.circle(surface_dude, COLORS['BLUE'], (375, 220), 10)

    pygame.draw.line(surface_dude, COLORS['BLACK'], (340, 300), (210, 410), 3)
    pygame.draw.line(surface_dude, COLORS['BLACK'], (420, 300), (600, 410), 3)
    pygame.draw.line(surface_dude, COLORS['BLACK'], (330, 520), (250, 700), 3)
    pygame.draw.line(surface_dude, COLORS['BLACK'], (200, 700), (250, 700), 3)
    pygame.draw.line(surface_dude, COLORS['BLACK'], (400, 520), (480, 700), 3)
    pygame.draw.line(surface_dude, COLORS['BLACK'], (530, 700), (480, 700), 3)
    surface_dude = pygame.transform.scale(surface_dude, size)
    surface_dude_2 = pygame.transform.flip(surface_dude, flip, False)
    screen.blit(surface_dude_2, cord)


def make_icecream(size, cord, tilt_angle):
    """
    param
    :param size: How much to compress a 2D drawing
    :param cord: drawing creation coordinates
    :param tilt_angle: The angle at which the drawing will be drawn
    :return: painted icecream
    """
    surface_icecream = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
    pygame.draw.polygon(surface_icecream, COLORS['ORANGE'], ((225, 425), (100, 400), (170, 330)))
    pygame.draw.circle(surface_icecream, COLORS['CHOCOLATE'], (110, 370), 30)
    pygame.draw.circle(surface_icecream, COLORS['CRIMSON'], (140, 340), 25)
    pygame.draw.circle(surface_icecream, COLORS['SNOW_COLOR'], (110, 335), 20)
    surface_icecream = pygame.transform.scale(surface_icecream, size)
    surface_icecream = pygame.transform.rotate(surface_icecream, tilt_angle)
    screen.blit(surface_icecream, cord)


def make_balloon(size, cord):
    """
    param
    :param size: How much to compress a 2D drawing
    :param cord: drawing creation coordinates
    :return: painted balloon
    """
    surface_balloon = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
    pygame.draw.polygon(surface_balloon, COLORS['RED'], ((920, 100), (1050, 140), (950, 250)))
    pygame.draw.circle(surface_balloon, COLORS['RED'], (960, 100), 40)
    pygame.draw.circle(surface_balloon, COLORS['RED'], (1025, 110), 40)
    pygame.draw.line(surface_balloon, COLORS['BLACK'], (950, 250), (940, 450), 3)
    surface_balloon = pygame.transform.scale(surface_balloon, size)
    surface_balloon = pygame.transform.flip(surface_balloon, True, False)
    screen.blit(surface_balloon, cord)


# background
def background():
    """
    this function draw background
    """
    pygame.draw.rect(screen, (122, 215, 255), (0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1]/2))
    pygame.draw.rect(screen, (91, 235, 111), (0, 400, WINDOW_SIZE[0], WINDOW_SIZE[1]/2))

background()
make_girl((750, 500), (0, 150), False)
make_girl((750, 500), (437, 150), True)

make_dude((750, 500), (0, 150), False)
make_dude((750, 500), (434, 150), True)

make_icecream((750, 500), (817, 268), 270)
make_balloon((750, 500), (-30, 130))

pygame.draw.line(screen, COLORS['BLACK'], (610, 200), (590, 345), 3)
make_icecream((1200, 800), (170, -200), 300)

for i in range(10):
    make_girl((750 - 10* i, 500- 10*i), (70 * i, 150+60 * i), False)
    make_girl((750 - 10* i, 500- 10*i), (437 + 70 * i , 150+60 * i), True)
    make_dude((750 - 10* i, 500- 10*i), (70 * i, 150+60 * i), False)
    make_dude((750 - 10* i, 500- 10*i), (434 + 70 * i, 150+60 * i), True)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
