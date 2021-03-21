#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from src.collision import bloque_sur_collision
from src.dessin import dessiner_niveau
from src.settings import JAUNE, BLEU_NUIT, NIVEAU, GRAVITE, TAILLE_FENETRE

pygame.init()
fenetre_rect = pygame.Rect((0, 0), TAILLE_FENETRE)
screen_surface = pygame.display.set_mode(TAILLE_FENETRE)

timer = pygame.time.Clock()

joueur = pygame.Surface((25, 25))
joueur.fill(JAUNE)
# Position du joueur
x, y = 25, 100
# Vitesse du joueur
vx, vy = 0, 0

# Boucle événementielle
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                vy = -20

    # Update de la position
    keys_pressed = pygame.key.get_pressed()
    old_x, old_y = x, y
    vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5
    vy += GRAVITE
    vy = min(20, vy)  # vy ne peut pas dépasser 25 sinon effet tunnel...
    x += vx
    y += vy
    x, y, vx, vy = bloque_sur_collision(NIVEAU, (old_x, old_y), (x, y), vx, vy)

    # Dessin
    screen_surface.fill(BLEU_NUIT)
    dessiner_niveau(screen_surface, NIVEAU)
    screen_surface.blit(joueur, (x, y))
    pygame.display.flip()
    timer.tick(30)

pygame.quit()
