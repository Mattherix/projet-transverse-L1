import sys, time, pygame
from pygame import time
from math import tan, cos

pygame.init()

FPS = 1
SIZE = width, height = 1000, 500

speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(SIZE)
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()


def pos_projectile(x, v, g, angle):
    """Position du projectile

    :param x: x(t) = v * cos(a) * t
    :param v: la vitesse initiale, à laquelle le projectile est lancé, en m/s
    :param g: l'accélération de la pesanteur en m/s2 (9,81 m/s2 à la surface de la Terre)
    :param angle: l'angle de portée, c'est-à-dire l'angle avec lequel le projectile est lancé, en degrés
    :return:
    """
    return (- g / ((2 * v) ** 2) * ((cos(angle)) ** 2)) * (x ** 2) + tan(angle) * x


x = 0
v = 1
g = 9.81
angle = 30
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x += 1
    ballrect.x = x
    ballrect.y = pos_projectile(x, v, g, angle)

    screen.fill(black)
    screen.blit(ball, ballrect)
    time = clock.tick(FPS)
    pygame.display.flip()

"""
class Slingshot :
    def init (self, x, y, w, h, color = (100, 200, 100)) :
    self.x = x
    self.y = y
    

"""
