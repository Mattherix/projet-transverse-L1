import pygame
from pygame.locals import *

pygame.init ()
fenetre = pygame.display.set_mode ((600, 600), RESIZABLE)
fond = pygame.image.load ('assets/space1.png').convert ()
fenetre.blit (fond, (0, 0))

# slingshot = pygame.image.load("assets/catapulte.jpg").convert()
# fenetre.blit(slingshot, (100,100))

color = pygame.Color (255, 255, 255)
pygame.draw.rect (fenetre, color, (250, 500, 100, 10))

pygame.display.flip ()

while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
            print ("End")

def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        # rectB est au-dessus
        return False
    if rectB.left > rectA.right:
        # rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        # rectB est en-dessous
        return False
    # Dans tous les autres cas il y a collision
    return True

