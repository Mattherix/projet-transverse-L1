"""Les object catapulte et jauge"""
from math import ceil

import pygame

from settings import GRIS, JAUNE, TAILLE_FENETRE, VERT


class Jauge:
    def __init__(self, pos=((0, TAILLE_FENETRE[1] - 20), (TAILLE_FENETRE[0], TAILLE_FENETRE[1])), loading=0,
                 background_color=GRIS, loading_color=JAUNE):
        self.pos = pos  # (x1, y1), (x2, y2)
        self.loading_percent = loading
        self.loading_pixel = ceil((self.pos[1][0] * self.loading_percent) / 100)
        self.background_color = background_color
        self.loading_color = loading_color

    def draw(self, surface):
        self.loading_pixel = ceil((self.pos[1][0] * self.loading_percent) / 100)
        pygame.draw.rect(surface, self.loading_color,
                         (self.pos[0][0], self.pos[0][1], self.loading_pixel, self.pos[1][1])
                         )

        pygame.draw.rect(surface, self.background_color,
                         (self.pos[0][0] + self.loading_pixel, self.pos[0][1], self.pos[1][0], self.pos[1][1])
                         )


class Catapulte:
    def __init__(self, color=VERT, fil=GRIS):
        self.color = color
        self.fil = fil

    def draw(self, screen_surface, loaded=None):
        pygame.draw.rect(screen_surface, self.color, (100, 540, 20, 60))
        if not (loaded is None) and loaded.loaded:
            pygame.draw.line(screen_surface, self.fil, (100, 560))
            pygame.draw.line(screen_surface, self.fil, (100, 540))
        pygame.draw.rect(screen_surface, self.color, (80, 500, 20, 50))
        pygame.draw.rect(screen_surface, self.color, (120, 500, 20, 50))
