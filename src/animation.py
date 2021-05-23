import pygame as pg
from os import path


class AnimatedSprite(pg.sprite.Sprite):

    def __init__(self, name, lenght):
        super().__init__()
        self.current_image = 0
        self.lenght = lenght
        self.images = load_sprite_sheet(name, self.lenght)
        self.image = self.images[self.current_image]

    def animate(self):
        # On actualise le numero de l'image actuel de l'animation
        self.current_image += 1
        self.current_image %= self.lenght

        self.image = self.images[self.current_image]


def load_sprite_sheet(name, lenght):
    sprites_path = path.join('assets', name)
    images = []
    for num in range(1, lenght+1):
        image_path = sprites_path + str(num) + '.png'
        images.append(pg.image.load(image_path))

    return images
