from math import cos, tan, sin

import pygame
from pygame.locals import K_RIGHT, K_LEFT, K_SPACE

from src.collisions import bloque_sur_collision
from src.settings import GRAVITE, NIVEAU, CONSTANTE_GRAVITATIONNEL, FPS


class Joueur:
    def __init__(self, x, y, w, h, vitesse=10, g=CONSTANTE_GRAVITATIONNEL, angle=10, color=(66, 73, 73)):
        # Position du joueur
        self.blocked = 0
        self.x = x
        self.y = y
        # Vitesse du joueur
        self.vx = 0
        self.vy = 0

        self.t = 0
        self.w = w
        self.h = h
        self.vitesse = vitesse
        self.g = g
        self.angle = angle
        self.h = h
        self.color = color

    def pos_projectile(self):
        """Position du projectile

        :param x: x(t) = v * cos(a) * t
        :param vitesse: la vitesse initiale, à laquelle le projectile est lancé, en m/s
        :param g: l'accélération de la pesanteur en m/s2 (9,81 m/s2 à la surface de la Terre)
        :param angle: l'angle de portée, c'est-à-dire l'angle avec lequel le projectile est lancé, en degrés
        :return:
        """
        # return (- self.g) / ((2 * self.v) ** 2 * cos(self.angle) ** 2) * self.x ** 2 + tan(self.angle) * self.x
        return -(- self.g / ((2 * self.vitesse) ** 2) * ((cos(self.angle)) ** 2)) * (self.x ** 2) + tan(
            self.angle) * self.x

    def next_position(self, x):
        self.x = self.x + x
        self.y = self.pos_projectile()

    def draw(self, surface):
        joueur = pygame.image.load('assets/balle.jpg').convert_alpha()
        joueur.set_colorkey((255, 255, 255))  # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
        surface.blit(joueur, (self.x, self.y))

    def position(self, keys_pressed):
        old_x, old_y = self.x, self.y
        if self.blocked != 0:
            self.vx = -1 * self.sens * self.vitesse * cos(3.14 - self.angle)
            self.vy = GRAVITE * self.t - self.vitesse * cos(3.14 - self.angle)

            self.t += 1
            self.blocked -= 1
        else:
            if keys_pressed[K_SPACE]:
                self.blocked = FPS * 5  # Bloquer pour 5s
                self.sens = -1 * ((keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) // 1)
                self.t = 0
            self.vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5

        if not self.blocked:
            self.vy += GRAVITE
        self.vy = min(20, self.vy)  # vy ne peut pas dépasser 25 sinon effet tunnel...

        self.x += self.vx
        self.y += self.vy
        self.x, self.y, self.vx, self.vy = bloque_sur_collision(NIVEAU, (old_x, old_y), (self.x, self.y), self.vx,
                                                                self.vy)
