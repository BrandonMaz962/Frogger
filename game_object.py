import pygame as pg

"""
    "Frog Jump" (Frogger Clone)
    Authors:
        Dustin Ecker
        Brandon Mazurkiewicz
"""

class Player(pg.sprite.Sprite):
    """ Class for handling the Player sprite loading/animation, movement, and collisions.

    Attributes:
        image: A pygame Image object.
        rect: A pygame Rect object.
        vehicles: A pygame sprite Group that holds all vehicles.
        obstacles: A pygame sprite Group that holds all static obstacles.
        powerups: A pygame sprite Group that holds on powerups (flies).
        event: A pygame event type for handling keypresses and player movement.
        won: Boolean to hold whether the player won or lost the game.
        jumpCount: Integer to hold amount of jumps it took the player to finish.
        flies_eaten: Integer to hold the number of flies the player ate to subtract from total time at the end.
    """
    def __init__(self, vehicles, obstacles, powerups):
        """ Initializes the instance of a Player.

        :param vehicles: Pygame sprite Group of vehicles.
        :param obstacles: Pygame sprite Group of obstacles.
        :param powerups: Pygame sprite Group of powerups.
        """
        super(Player, self).__init__()
        self.image = pg.image.load("./assets/frog.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.centery = 495
        self.vehicles = vehicles
        self.obstacles = obstacles
        self.powerups = powerups
        self.event = pg.USEREVENT + 1
        self.won = False
        self.jumpCount = 0
        self.flies_eaten = 0

    def update(self, delta):
        """ Used for updating the sprite and position if the player is blocked by an obstacle or
            has a collision.

        :param delta: Used for smoothing transitions and animations.
        """
        collision = pg.sprite.spritecollideany(self, self.vehicles)
        if collision:
            collision.kill()
            pg.event.post(pg.event.Event(self.event))
            self.kill()

        powered = pg.sprite.spritecollideany(self, self.powerups)
        if powered:
            powered.kill()
            powered.eaten = True

        blocked = pg.sprite.spritecollideany(self, self.obstacles)
        if blocked:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y + 1
        if self.rect.y <= 0:
            self.kill()
            self.setWon(True)

    def setImage(self, image):
        """ Sets the image of the Player.

        :param image: A pygame Image object.
        """
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (30, 30))

    def setWon(self, won):
        """ Sets the win boolean.

        :param won: Boolean for if the player has won the game.
        """
        self.won = won

    def getWon(self):
        """ Gets the win boolean.

        :return: Returns whether the player has won the game or not.
        """
        return self.won

    def up(self, delta):
        """ Handles sprite movement for if the player presses the up (W) key.

        :param delta: Used for smoothing transitions and animations.
        """
        pg.display.update()
        if self.rect.y - 20 < 0:
            self.rect.y = 0
        else:
            self.rect.y -= 20

    def down(self, delta):
        """ Handles sprite movement for if the player presses the down (S) key.

        :param delta: Used for smoothing transitions and animations.
        """
        pg.display.update()
        if self.rect.y + 20 > 480:
            self.rect.y = 480
        else:
            self.rect.y += 20

    def left(self, delta):
        """ Handles sprite movement for if the player presses the left (A) key.

        :param delta: Used for smoothing transitions and animations.
        """
        if self.rect.x - 25 < 5:
            self.rect.x = 5
        else:
            self.rect.x -= 25

    def right(self, delta):
        """ Handles sprite movement for if the player presses the right (D) key.

        :param delta: Used for smoothing transitions and animations.
        """
        if self.rect.x + 25 > 560:
            self.rect.x = 560
        else:
            self.rect.x += 25
