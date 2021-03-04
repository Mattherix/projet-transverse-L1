import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((600, 600), RESIZABLE)
fond = pygame.image.load('assets/space1.png').convert()
fenetre.blit(fond, (0,0))

#slingshot = pygame.image.load("assets/catapulte.jpg").convert()
#fenetre.blit(slingshot, (100,100))

color = pygame.Color(255, 255, 255)
pygame.draw.rect(fenetre, color, (250,500,100,10))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("End")