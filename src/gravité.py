#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame import display
from pygame.locals import QUIT, KEYDOWN, K_SPACE

from catapulte_jauge import Jauge
from src.dessin import dessiner_niveau
from src.joueur import Joueur
from src.settings import NIVEAU, TAILLE_FENETRE, TITRE_FENETRE, FPS

pygame.init()


pygame.mixer.init()
pygame.mixer.music.load("music_and_sound/[04] Flowering Night.flac")
pygame.mixer.music.play(-1)


fenetre_rect = pygame.Rect((0, 0), TAILLE_FENETRE)
screen_surface = pygame.display.set_mode(TAILLE_FENETRE)
display.set_caption(TITRE_FENETRE)

timer = pygame.time.Clock()


background = pygame.image.load('assets/space1.png')
# Position du joueur
x, y = 25, 100

joueur = Joueur(x, y, 20, 20)
jauge = Jauge()

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
    joueur.position(keys_pressed)

    # Dessin
    screen_surface.blit(background, (0, 0))
    dessiner_niveau(screen_surface, NIVEAU)
    joueur.draw(screen_surface)

    jauge.loading_percent += 1
    jauge.draw(screen_surface)


    pygame.display.flip()
    timer.tick(FPS)

pygame.quit()
