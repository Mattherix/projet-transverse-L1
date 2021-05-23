import pygame as pg
from os import path


class AnimatedSprite(pg.sprite.Sprite):

    def __init__(self, name, lenght, frame_per_image):
        super().__init__()
        self.current_image = 0
        self.lenght = lenght
        self.frame_per_image = frame_per_image
        self.image_counter = frame_per_image
        self.images = load_sprite_sheet(name, self.lenght)
        self.image = self.images[self.current_image]

    def animate(self, flip=False):
        # On actualise le numero de l'image actuel de l'animation
        if not self.image_counter:
            self.current_image += 1
            self.current_image %= self.lenght

            self.image = pg.transform.flip(self.images[self.current_image], flip, False)

            self.image_counter = self.frame_per_image
        else:
            self.image_counter -= 1


def load_sprite_sheet(name, lenght):
    sprites_path = path.join('assets', name)
    images = []
    for num in range(1, lenght+1):
        image_path = sprites_path + str(num) + '.png'
        images.append(pg.image.load(image_path))

    return images
