import pygame
from math import ceil
from settings import GRIS, JAUNE, TAILLE_FENETRE


class Jauge:
    def __init__(self, pos=((0, TAILLE_FENETRE[1] - 20), (TAILLE_FENETRE[0], TAILLE_FENETRE[1])), loading=0, background_color=GRIS, loading_color=JAUNE):
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
