import os
import pygame as pg

"""
    "Frog Jump" (Frogger Clone)
    Authors:
        Dustin Ecker
        Brandon Mazurkiewicz
"""

class Vehicle(pg.sprite.Sprite):
    """ Class for handling the Vehicle sprite loading and movement.

    Attributes:
        image: A pygame Image object.
        rect: A pygame Rect object.
        startLocation: An X/Y coordinate for the start location of the vehicle.
        direction: Integer for determining whether the vehicle travels left or right on the screen (-1 left, 1 right).
        speed: Integer to determine the speed the vehicles travels across the screen.
    """
    def __init__(self, startLocation, image, speed, direction, size):
        """ Initializes the instance of a vehicle.

        :param startLocation: An X/Y coordinate for the start location of the vehicle.
        :param image: A pygame Image object.
        :param speed: Integer to determine the speed the vehicles travels across the screen.
        :param direction: Integer for determining whether the vehicle travels left or right on the screen (-1 left, 1 right).
        :param size: An X/Y pixel size for the sprite.
        """
        super(Vehicle, self).__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self.startLocation = startLocation
        self.direction = direction
        self.speed = speed

    def draw(self, screen):
        """ Used for drawing the sprite to the screen.

        :param screen: Passes in the screen object to draw the sprite to.
        """
        screen.blit(self.image, self.rect)

    def update(self, delta):
        """ Used for updating the sprite and position as the vehicle travels across the screen.

        :param delta: Used for smoothing transitions and animations.
        """
        self.rect.y += 100 * delta * self.direction
        if self.rect.y > self.startLocation[1] + 100 or self.rect.y < self.startLocation[1] - 100:
            self.direction *= -1

    def move(self, delta):
        """ Used for moving a vehicle across the screen, and recycling the sprite as it exits one side of the screen
            and reappears on the other side.

        :param delta: Used for smoothing transitions and animations.
        """
        self.rect.x += self.speed * delta * self.direction
        if self.rect.x < 0 - self.image.get_width():
            self.rect.x = 600 + self.image.get_width()
        if self.rect.x > 600 + self.image.get_width():
            self.rect.x = 0 - self.image.get_width()


class Obstacle(pg.sprite.Sprite):
    """ Class for handling the Obstacle sprite loading.

    Attributes:
        image: A pygame Image object.
        rect: A pygame Rect object.
        startLocation: An X/Y coordinate for the start location of the obstacle.
        direction: Integer for determining whether the objects direction. (unused).
    """
    def __init__(self, startLocation, image):
        super(Obstacle, self).__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self.startLocation = startLocation
        self.direction = 1

    def draw(self, screen):
        """ Used for drawing the sprite to the screen.

        :param screen: Passes in the screen object to draw the sprite to.
        """
        screen.blit(self.image, self.rect)

    def update(self, delta):
        """ Used for updating the sprite of the obstacle.

        :param delta: Used for smoothing transitions and animations.
        """
        pass
