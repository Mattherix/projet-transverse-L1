import pygame

from src.settings import VERT


mur = pygame.Surface((25, 25))
mur.fill(VERT)


def dessiner_niveau(surface, niveau):
    """Dessine le niveau sur la surface donnée.

    Utilise la surface `mur` pour dessiner les cases de valeur 1
    """
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                surface.blit(mur, (i * 25, j * 25))
