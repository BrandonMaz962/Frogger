import os
import pygame as pg

"""
    "Frog Jump" (Frogger Clone)
    Authors:
        Dustin Ecker
        Brandon Mazurkiewicz
"""

class Fly(pg.sprite.Sprite):
    """ Class for handling the Fly sprite loading and repositioning.

    Attributes:
        image: A pygame Image object.
        rect: A pygame Rect object.
        startLocation: An X/Y coordinate for the start location of the vehicle.
        eaten: Boolean to determine whether the fly has been eaten or not.
    """
    def __init__(self, startLocation, image):
        """ Initializes the instance of a fly.

        :param startLocation: An X/Y coordinate for the start location of the vehicle.
        :param image: A pygame Image object.
        """
        super(Fly, self).__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self.startLocation = startLocation
        self.eaten = False

    def draw(self, screen):
        """ Used for drawing the sprite to the screen.

        :param screen: Passes in the screen object to draw the sprite to.
        """
        screen.blit(self.image, self.rect)

    def update(self, delta):
        """ Used for updating the sprite of the fly.

        :param delta: Used for smoothing transitions and animations.
        """
        pass
