import os
import pygame as pg

"""
    "Frog Jump" (Frogger Clone)
    Authors:
        Dustin Ecker
        Brandon Mazurkiewicz
"""

class Background(pg.sprite.Sprite):
    """ Class for handling the Background sprite loading.

    Attributes:
        image: A pygame Image object.
        rect: A pygame Rect object.
    """
    def __init__(self):
        """ Initializes the instance of the background.

        :param image: A pygame Image object.
        :param rect: A pygame Rect object.
        """
        super(Background, self).__init__()
        self.image = pg.image.load("assets/background-roadsonly-withwater.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.centery = 274

    def update(self, delta):
        """ Used for updating the sprite of the background.

        :param delta: Used for smoothing transitions and animations.
        """
        pass
