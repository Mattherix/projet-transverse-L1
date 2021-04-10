"""La classe du joueur"""
from math import cos, tan

import pygame
from pygame.locals import K_RIGHT, K_LEFT, K_SPACE

from catapulte_jauge import Jauge
from collisions import bloque_sur_collision
from settings import GRAVITE, NIVEAU, CONSTANTE_GRAVITATIONNEL


class Joueur:
    def __init__(self, x, y, w, h, vitesse=10, g=CONSTANTE_GRAVITATIONNEL, angle=10, color=(66, 73, 73)):
        # Position du joueur
        self.in_mouvment = False
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
        self.sens = 0

        self.jauge = Jauge()
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
        self.jauge.draw(surface)

    def position(self, keys_pressed):
        old_x, old_y = self.x, self.y
        # Le joueur est soit en vole, soit en train de charger son catapultage, soit il se déplace horizontalement
        if keys_pressed[K_SPACE] and self.jauge.loading_percent < 100:
            self.sens = -1 * ((keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) // 1)  # A droite ou à gauche ?
            self.t = 0
            self.jauge.loading_percent += 1

            self.vitesse = self.jauge.loading_percent / 5
        elif not self.in_mouvment:
            self.vx = -1 * self.sens * self.vitesse * cos(3.14 - self.angle)
            self.vy = GRAVITE * self.t - self.vitesse * cos(3.14 - self.angle)

            self.t += 1
        else:
            self.vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5
            self.jauge.loading_percent = 0

        if self.in_mouvment:
            self.vy += GRAVITE
        self.vy = min(20, self.vy)  # vy ne peut pas dépasser 25 sinon effet tunnel...

        self.x += self.vx
        self.y += self.vy
        self.x, self.y, self.vx, self.vy = bloque_sur_collision(NIVEAU, (old_x, old_y), (self.x, self.y), self.vx,
                                                                self.vy)

        if (self.x - old_x) < 0.01 and (self.y - old_y) < 0.01:
            self.in_mouvment = False
        else:
            self.in_mouvment = True
