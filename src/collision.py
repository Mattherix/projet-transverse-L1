"""Fonction s'occupant des collisions"""

import pygame

from src.settings import BLOCK_LENGHT, BLOCK_HEIGHT


def from_coord_to_grid(pos):
    """Retourne la position dans le niveau en indice (i, j)

    `pos` est un tuple contenant la position (x, y) du coin supérieur gauche.
    On limite i et j à être positif.
    """
    x, y = pos
    i = max(0, int(x // BLOCK_LENGHT))
    j = max(0, int(y // BLOCK_HEIGHT))
    return i, j


def get_neighbour_blocks(niveau, i_start, j_start):
    """Retourne la liste des rectangles autour de la position (i_start, j_start).

    Vu que le personnage est dans le carré (i_start, j_start), il ne peut
    entrer en collision qu'avec des blocks dans sa case, la case en-dessous,
    la case à droite ou celle en bas et à droite. On ne prend en compte que
    les cases du niveau avec une valeur de 1.
    """
    blocks = list()
    for j in range(j_start, j_start + 2):
        for i in range(i_start, i_start + 2):
            try:
                if niveau[j][i] == 1:
                    topleft = i * BLOCK_LENGHT, j * BLOCK_HEIGHT
                    blocks.append(pygame.Rect(topleft, (BLOCK_LENGHT, BLOCK_HEIGHT)))
            except IndexError:
                # Il n'y a pas de blocks de ce coté
                pass
    return blocks


def bloque_sur_collision(niveau, old_pos, new_pos, vx, vy):
    """Tente de déplacer old_pos vers new_pos dans le niveau.

    S'il y a collision avec les éléments du niveau, new_pos sera ajusté pour
    être adjacents aux éléments avec lesquels il entre en collision.
    On passe également en argument les vitesses `vx` et `vy`.

    La fonction retourne la position modifiée pour new_pos ainsi que les
    vitesses modifiées selon les éventuelles collisions.
    """
    old_rect = pygame.Rect(old_pos, (BLOCK_LENGHT, BLOCK_HEIGHT))
    new_rect = pygame.Rect(new_pos, (BLOCK_LENGHT, BLOCK_HEIGHT))
    i, j = from_coord_to_grid(new_pos)
    collide_later = list()
    blocks = get_neighbour_blocks(niveau, i, j)
    for block in blocks:
        if not new_rect.colliderect(block):
            continue

        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect)
        # Dans cette première phase, on n'ajuste que les pénétrations sur un
        # seul axe.
        if dx_correction == 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dy_correction == 0.0:
            new_rect.left += dx_correction
            vx = 0.0
        else:
            collide_later.append(block)

    # Deuxième phase. On teste à présent les distances de pénétrations pour
    # les blocks qui en possédaient sur les 2 axes.
    for block in collide_later:
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect)
        if dx_correction == dy_correction == 0.0:
            # Finalement plus de pénétration. Le new_rect a bougé précédemment
            # lors d'une résolution de collision
            continue
        if abs(dx_correction) < abs(dy_correction):
            # Faire la correction que sur l'axe X (plus bas)
            dy_correction = 0.0
        elif abs(dy_correction) < abs(dx_correction):
            # Faire la correction que sur l'axe Y (plus bas)
            dx_correction = 0.0
        if dy_correction != 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dx_correction != 0.0:
            new_rect.left += dx_correction
            vx = 0.0

    x, y = new_rect.topleft
    return x, y, vx, vy


def compute_penetration(block, old_rect, new_rect):
    """Calcul la distance de pénétration du `new_rect` dans le `block` donné.

    `block`, `old_rect` et `new_rect` sont des pygame.Rect.
    Retourne les distances `dx_correction` et `dy_correction`.
    """
    dx_correction = dy_correction = 0.0
    if old_rect.bottom <= block.top < new_rect.bottom:
        dy_correction = block.top - new_rect.bottom
    elif old_rect.top >= block.bottom > new_rect.top:
        dy_correction = block.bottom - new_rect.top
    if old_rect.right <= block.left < new_rect.right:
        dx_correction = block.left - new_rect.right
    elif old_rect.left >= block.right > new_rect.left:
        dx_correction = block.right - new_rect.left
    return dx_correction, dy_correction
