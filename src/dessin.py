import pygame

from src.settings import VERT, BLOCK_HEIGHT, BLOCK_LENGHT

mur = pygame.Surface((BLOCK_LENGHT, BLOCK_HEIGHT))
mur.fill(VERT)


def dessiner_niveau(surface, niveau):
    """Dessine le niveau sur la surface donnée.

    Utilise la surface `mur` pour dessiner les cases de valeur 1
    """
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                surface.blit(mur, (i * BLOCK_LENGHT, j * BLOCK_HEIGHT))
