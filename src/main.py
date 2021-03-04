from math import cos, tan
from time import sleep

import pygame
from pygame import display

pygame.init()


display.init()


class Perso:
    def __init__(self, x, y, w, h, v=10, g=9.81, angle=10, color=(66, 73, 73)):
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
        # return (- self.g) / ((2 * self.v) ** 2 * cos(self.angle) ** 2) * self.x ** 2 + tan(self.angle) * self.x
        return -(- self.g / ((2 * self.v) ** 2) * ((cos(self.angle)) ** 2)) * (self.x ** 2) + tan(self.angle) * self.x

    def next_position(self, x):
        self.x = self.x + x
        self.y = self.pos_projectile()

    def draw(self, surface, loaded=None):
        pygame.draw.rect(surface, self.color, (self.x, self.y + self.h * 1 / 3, self.w, self.h * 2 / 3))


display.set_caption("TheGame")
screen = display.set_mode((1080, 720))

background = pygame.image.load('assets/space1.png')

v = int(input("Vitesse: "))
angle = int(input("Angle: "))
sleep(3)

surface = display.get_surface()
p = Perso(100, 500, 20, 20, v=v, angle=angle)
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
    display.update()
