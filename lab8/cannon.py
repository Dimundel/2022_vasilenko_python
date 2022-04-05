import math
import random

import pygame

pygame.init()

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
DARK_GREY = 0x2F2F2F
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FONT = pygame.font.SysFont("Comic Sans MS", 32)

WIDTH = 800
HEIGHT = 600

NUM_OF_TARGETS = 3
GRAVITY_ACCELERATION = 3
AIR_RESISTANCE = 1 / 100


class CannonBall:
    """Cannonballs which are shot by gus"""

    def __init__(self, the_screen, x, y):
        self.screen = the_screen
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = random.choice(GAME_COLORS)
        self.live = 150

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """checks collisions between self and obj"""
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True

        return False

    def lose_live(self, bullets_list):
        """destroys self after period of time"""
        self.live -= 1
        if self.live <= 0:
            bullets_list.remove(self)


class Projectile(CannonBall):
    def move(self):
        self.vx += -abs(AIR_RESISTANCE) * self.vx
        self.x += self.vx
        self.vy += GRAVITY_ACCELERATION - abs(AIR_RESISTANCE) * self.vy
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

        self.lose_live(bullets)


class Hitscan(CannonBall):
    def __init__(self, the_screen, x, y):
        CannonBall.__init__(self, the_screen, x, y)
        self.r = 5
        self.vx = 50

    def move(self):
        self.x += self.vx
        self.y += self.vy


class Gun:
    def __init__(self, the_screen, x, y):
        self.x = x
        self.y = y
        self.screen = the_screen
        self.angle = 0
        self.color = GREY
        self.r = 20


class PlayerGun(Gun):
    def __init__(self, the_screen):
        Gun.__init__(self, the_screen, 0, pygame.mouse.get_pos()[1])
        self.f2_power = 10
        self.f2_on = False
        self.color = GREY
        self.f2_power = 10
        self.f2_on = False

    def move(self):
        """moves gun while mouse is not pressed"""
        if not pygame.mouse.get_pressed()[0]:
            self.y = pygame.mouse.get_pos()[1]

    def fire2_start(self):
        """starts gun targetting"""
        self.f2_on = True

    def fire2_end(self, cannonball_type, balls_array, bullets_num):
        """shoots cannonball"""
        bullets_num += 1
        new_ball = cannonball_type(self.screen, self.x + self.r + 4, self.y)

        if cannonball_type == Projectile:
            new_ball.vx = self.f2_power * math.cos(self.angle)
            new_ball.vy = self.f2_power * math.sin(self.angle)

        balls_array.append(new_ball)
        self.f2_on = False
        self.f2_power = 10

    def targetting(self, the_event):
        """does gun targetting animation"""
        if the_event:
            if the_event.pos[0] - self.x != 0:
                self.angle = math.atan((the_event.pos[1] - self.y) / (the_event.pos[0] - self.x))
            else:
                self.angle = math.pi / 2
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(screen, self.color, (self.x, self.y),
                         (self.x + self.f2_power * math.cos(self.angle), self.y + self.f2_power * math.sin(self.angle)),
                         width=10)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def power_up(self):
        """increases start velocity of cannonball"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class EnemyGun(Gun):
    def __init__(self, the_screen, x, y):
        Gun.__init__(self, the_screen, x, y)
        self.color = DARK_GREY
        self.v = 20

    def shoot(self, balls_array, the_player):
        """shoots to player's gun coordinates"""
        to_shoot = random.randint(0, 30)
        if not to_shoot:
            angle = -math.atan((the_player.y - self.y) / (the_player.x - self.x)) - math.pi / 2
            new_ball = Hitscan(self.screen, self.x, self.y)
            balls_array.append(new_ball)
            new_ball.vy = self.v * math.cos(angle)
            new_ball.vx = self.v * math.sin(angle)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


class Target:
    def __init__(self, the_screen):
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
        self.y += self.vy

    def new_target(self):
        """re-creates the target"""
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.vy = random.randint(1, 10)
        self.r = random.randint(5, 50)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r, 2)


class NormalTarget(Target):
    def __init__(self, the_screen):
        Target.__init__(self, the_screen)
        self.color = RED


class ChaoticTarget(Target):
    def __init__(self, the_screen):
        Target.__init__(self, the_screen)
        self.color = BLUE

    def move(self):
        Target.move(self)
        self.y += self.vy
        to_change_direction = random.randint(0, 30)
        if not to_change_direction:
            self.vy = -self.vy


class DissapearingTarget(Target):
    def __init__(self, the_screen):
        Target.__init__(self, the_screen)
        self.color = GREEN
        self.is_visible = True

    def move(self):
        Target.move(self)
        to_dissappear = random.randint(0, 30)
        if not to_dissappear:
            self.is_visible = not self.is_visible

    def draw(self):
        if self.is_visible:
            Target.draw(self)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
num_bullets = 0
score = 0
bullets = []
targets = []
enemy_guns = []

clock = pygame.time.Clock()
player_gun = PlayerGun(screen)
enemy_gun1 = EnemyGun(screen, 400, 0)
enemy_gun2 = EnemyGun(screen, 400, 600)
enemy_guns.append(enemy_gun1)
enemy_guns.append(enemy_gun2)

new_target = NormalTarget(screen)
targets.append(new_target)
new_target = ChaoticTarget(screen)
targets.append(new_target)
new_target = DissapearingTarget(screen)
targets.append(new_target)

finished = False


def draw():
    player_gun.draw()

    for the_target in targets:
        the_target.draw()

    for the_b in bullets:
        the_b.draw()

    for the_enemy_gun in enemy_guns:
        the_enemy_gun.draw()


def game_processing(the_score, the_finished):
    """moves cannonballs, guns, targets, checks collisions"""
    for the_b in bullets:
        the_b.move()
        for the_target in targets:
            if the_b.hittest(the_target):
                the_target.new_target()
                the_score += 1
            if the_b.hittest(player_gun):
                the_finished = True

    for the_target in targets:
        the_target.move()

    for the_enemy_gun in enemy_guns:
        the_enemy_gun.shoot(bullets, player_gun)

    player_gun.move()
    player_gun.power_up()

    return the_score, the_finished


while not finished:
    screen.fill(WHITE)

    score_surface = FONT.render("Score: {}".format(score), False, BLACK)
    screen.blit(score_surface, (0, 0))

    draw()

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                player_gun.fire2_end(Projectile, bullets, num_bullets)
            elif event.button == 3:
                player_gun.fire2_end(Hitscan, bullets, num_bullets)
        elif event.type == pygame.MOUSEMOTION:
            player_gun.targetting(event)

    score, finished = game_processing(score, finished)

pygame.quit()

print("Game Over!")
print("Your score: {}".format(score))
