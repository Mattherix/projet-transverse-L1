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


class Slingshot:
    def __init__(self, x, y, w, h, color=(66, 73, 73)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def rotate(self, coord, angle, anchor=(0, 0)):
        corr = 0
        return ((coord[0] - anchor[0])*cos(angle + radians(corr)) - (coord[1] - anchor[1])*sin(angle + radians(corr)),
                (coord[0] - anchor[0])*sin(angle + radians(corr)) + (coord[1] - anchor[1])*cos(angle + radians(corr)))

    def translate(self, coord):
        return [coord[0] + self.x, coord[1] + self.y]

    def draw(self, loaded=None):
        pygame.draw.rect(display, self.color, (self.x, self.y + self.h*1/3, self.w, self.h*2/3))

        if (not loaded == None) and loaded.loaded:
            pygame.draw.line(display, ( 100, 30, 22 ), (self.x - self.w/4 + self.w/4, self.y + self.h/6), (loaded.x, loaded.y + loaded.r/2), 10)
            pygame.draw.line(display, ( 100, 30, 22 ), (self.x + self.w, self.y + self.h/6), (loaded.x + loaded.r, loaded.y + loaded.r/2), 10)

        pygame.draw.rect(display, self.color, (self.x - self.w/4, self.y, self.w/2, self.h/3), 5)
        pygame.draw.rect(display, self.color, (self.x + self.w - self.w/4, self.y, self.w/2, self.h/3), 5)


"""
import pygame

pygame.init()

pygame.display.set_caption("TheGame")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/space1.png')

running = True

while running:
    # arriere plan du jeu,
    screen.blit(background, (0, 0))
    # mettre a jour l'écran
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("End")
