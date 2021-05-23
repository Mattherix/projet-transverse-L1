"""Tous les sprites du joueur"""
import random

import pygame as pg
from settings import *
from animation import AnimatedSprite

vec = pg.math.Vector2


class Player(AnimatedSprite):
    """La classe représentant le joueur"""

    def __init__(self, game):
        super().__init__("dino sheets/DinoSprites - doux - ", 10, FPS / 6)
        self.game = game
        self.images = [pg.transform.scale2x(image) for image in self.images]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.sens = False

    def jump(self):
        """Saut, lorsqu'il saute a partir d'une plateforme"""
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP

        self.game.play_sound(SOUNDS["jump"])

    def update(self):
        """Update de l'état du joueur"""
        self.acc = vec(0, PLAYER_GRAV)  # Application de la gravité sur le personnage
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC  # Application de la gravité sur le personnage
            self.sens = True
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC  # regarder les settings
            self.sens = False

        # application de la friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equation de trajectoire joueur
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # Pour pouvoir avoir le joueur qui passe d'un côté à l'autre
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos  # positionnement du personnage sur la plateforme au debut de la partie

        self.animate(self.sens)


class Platform(pg.sprite.Sprite):
    """La classe représentant les platformes"""

    def __init__(self, x, y, w, h):  # Parametre de la plateforme
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/Grass.png')
        self.image = pg.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cloud(Platform, AnimatedSprite):
    """Un nuage traversant l'écran"""
    def __init__(self, x, y, w, h):
        Platform.__init__(self, x, y, w, h)
        AnimatedSprite.__init__(self, "cloud/Cloud_", 2, FPS / 6)
        self.sens = random.randrange(0, 2)

    def update(self):
        if self.sens:
            self.rect.x += 1
            if self.rect.x > WIDTH:
                self.rect.x = 0
        else:
            self.rect.x -= 1
            if self.rect.x < 0:
                self.rect.x = WIDTH

        self.animate()
