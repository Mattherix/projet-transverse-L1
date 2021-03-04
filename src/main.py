"""import sys, time, pygame
from pygame import time, display
from math import tan, cos, sin, radians

pygame.init()

FPS = 1
SIZE = width, height = 1000, 500

speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(SIZE)
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()


def pos_projectile(x, v, g, angle):
    \"""Position du projectile

    :param x: x(t) = v * cos(a) * t
    :param v: la vitesse initiale, à laquelle le projectile est lancé, en m/s
    :param g: l'accélération de la pesanteur en m/s2 (9,81 m/s2 à la surface de la Terre)
    :param angle: l'angle de portée, c'est-à-dire l'angle avec lequel le projectile est lancé, en degrés
    :return:
    \"""
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
from math import cos, sin, radians, tan

from pygame import display

display.init()


class Perso:
    def __init__(self, x, y, w, h, v=10, g=9.81, angle=1, color=(66, 73, 73)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = v
        self.g = g
        self.angle = angle
        self.h = h
        self.color = color

    def pos_projectile(self):
        """Position du projectile

        :param x: x(t) = v * cos(a) * t
        :param v: la vitesse initiale, à laquelle le projectile est lancé, en m/s
        :param g: l'accélération de la pesanteur en m/s2 (9,81 m/s2 à la surface de la Terre)
        :param angle: l'angle de portée, c'est-à-dire l'angle avec lequel le projectile est lancé, en degrés
        :return:
        """
        return (- self.g / ((2 * self.v) ** 2) * ((cos(self.angle)) ** 2)) * (self.x ** 2) + tan(self.angle) * self.x

    def next_position(self, x):
        self.x = self.x + x
        self.y = self.pos_projectile()

    def draw(self, surface, loaded=None):
        pygame.draw.rect(surface, self.color, (self.x, self.y + self.h * 1 / 3, self.w, self.h * 2 / 3))

import pygame

pygame.init()

pygame.display.set_caption("TheGame")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/space1.png')

surface = display.get_surface()
p = Perso(100, 500, 20, 20)
clock = pygame.time.Clock()
while True:
    # arriere plan du jeu,
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("End")

    p.next_position(1)
    p.draw(surface)

    # mettre a jour l'écran
    time = clock.tick(60)
    pygame.display.update()
