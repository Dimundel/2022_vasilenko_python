import math
import random
from random import choice

import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

NUM_OF_TARGETS = 2
GRAVITY_ACCELERATION = 1


class Ball:
    def __init__(self, the_screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = the_screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.x += self.vx
        self.vy += GRAVITY_ACCELERATION
        self.y += self.vy

        if self.y >= HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.vy = - self.vy

        if self.y <= self.r:
            self.y = self.r
            self.vy = - self.vy

        if self.x >= WIDTH - self.r:
            self.x = WIDTH - self.r
            self.vx = - self.vx

        if self.x <= self.r:
            self.x = self.r
            self.vx = - self.vx

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x-obj.x)**2+(self.y-obj.y)**2 <= (self.r+obj.r)**2:
            return True

        return False


class Gun:
    def __init__(self, the_screen):
        self.screen = the_screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, the_event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((the_event.pos[1] - new_ball.y), (the_event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, the_event):
        """Прицеливание. Зависит от положения мыши."""
        if the_event:
            if the_event.pos[0] - 50 != 0:
                self.an = math.atan((the_event.pos[1] - 450) / (the_event.pos[0] - 50))
            else:
                self.an = math.pi / 2
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(screen, self.color, (40, 450),
                         (40 + self.f2_power * math.cos(self.an), 450 + self.f2_power * math.sin(self.an)), width=5)
        pygame.draw.circle(screen, self.color, (40, 450), 5)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, the_screen):
        self.points = 0
        self.x = None
        self.y = None
        self.vy = None
        self.r = None
        self.color = None
        self.screen = the_screen
        self.new_target()

    def move(self):
        if self.y <= self.r:
            self.y = self.r
            self.vy = - self.vy
        if self.y >= HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.vy = - self.vy
        self. y += self.vy

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.vy = random.randint(1, 10)
        self.r = random.randint(2, 50)
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r, 2)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []

clock = pygame.time.Clock()
gun = Gun(screen)

for target in range(NUM_OF_TARGETS):
    new_target = Target(screen)
    targets.append(new_target)

finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        for target in targets:
            if b.hittest(target):
                target.hit()
                target.new_target()
    for target in targets:
        target.move()
    gun.power_up()

pygame.quit()
