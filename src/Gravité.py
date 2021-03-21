#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

# On initialise pygame
from src.collision import bloque_sur_collision
from src.dessin import dessiner_niveau
from src.settings import JAUNE, BLEU_NUIT, NIVEAU

pygame.init()
taille_fenetre = (600, 400)
fenetre_rect = pygame.Rect((0, 0), taille_fenetre)
screen_surface = pygame.display.set_mode(taille_fenetre)



timer = pygame.time.Clock()

joueur = pygame.Surface((25, 25))
joueur.fill(JAUNE)
# Position du joueur
x, y = 25, 100
# Vitesse du joueur
vx, vy = 0, 0
# Gravité vers le bas donc positive
GRAVITE = 2




# Boucle événementielle
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                vy = -20

    timer.tick(30)
    keys_pressed = pygame.key.get_pressed()
    # Sauvegarde de l'ancienne position
    old_x, old_y = x, y
    vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5
    vy += GRAVITE
    vy = min(20, vy)  # vy ne peut pas dépasser 25 sinon effet tunnel...
    x += vx
    y += vy
    x, y, vx, vy = bloque_sur_collision(NIVEAU, (old_x, old_y), (x, y), vx, vy)

    screen_surface.fill(BLEU_NUIT)
    dessiner_niveau(screen_surface, NIVEAU)
    screen_surface.blit(joueur, (x, y))
    pygame.display.flip()

pygame.quit()
