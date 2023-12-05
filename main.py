import random

from game_object import *
from pygame.locals import *
from background import *
from hazard import *
from powerup import *
import pygame as pg

"""
    "Frog Jump" (Frogger Clone)
    Authors:
        Dustin Ecker
        Brandon Mazurkiewicz
"""

def main():
    """ The core loop of the game. Initializes the Player, Background, Hazards, and Powerups.
        Handles collisions and input from the user.
    """
    pg.init()
    screen = pg.display.set_mode([600, 550]) # was 478
    running = True
    paused = False
    clock = pg.time.Clock()
    delta = clock.tick(60) / 1000

    start_time = pg.time.get_ticks()

    our_go = pg.sprite.Group()
    vehicles = pg.sprite.Group()
    obstacles = pg.sprite.Group()
    powerups = pg.sprite.Group()

    p = Player(vehicles, obstacles, powerups)
    bg = Background()

    fly = Fly(randFly(), './assets/fly.png')
    powerups.add(fly)

    for i in range(0, 600, 225):
        car = Vehicle((i, 133), './assets/car.png', 40, 1, (60, 30))
        vehicles.add(car)

    for i in range(0, 600, 300):
        truck = Vehicle((i, 215), './assets/truck.png', 50, -1, (60, 30))
        vehicles.add(truck)

    police = Vehicle((300, 255), './assets/police_car.png', 70, -1, (60, 30))

    train = Vehicle((50, 333), './assets/train.png', 85, -1, (180, 30))

    for i in range(0, 600, 200):
        redCar = Vehicle((i, 413), './assets/red_car.png', 40, 1, (60, 30))
        vehicles.add(redCar)

    for i in range(0, 450, 175):
        firetruck = Vehicle((i, 455), './assets/firetruck.png', 50, -1, (60, 30))
        vehicles.add(firetruck)

    vehicles.add(police)
    vehicles.add(train)

    rock = Obstacle((150, 295), './assets/rock.png')
    rock2 = Obstacle((300, 295), './assets/rock.png')
    rock3 = Obstacle((500, 295), './assets/rock.png')
    tree = Obstacle((60, 92), './assets/log.png')
    tree2 = Obstacle((400, 92), './assets/log.png')

    obstacles.add(rock)
    obstacles.add(rock2)
    obstacles.add(rock3)
    obstacles.add(tree)
    obstacles.add(tree2)

    our_go.add(bg)
    our_go.add(p)
    our_go.add(fly)
    for x in vehicles:
        our_go.add(x)
    for y in obstacles:
        our_go.add(y)

    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/PublicPixel-z84yD.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    WHITE = (254, 254, 254)

    while running:
        for x in vehicles:
            x.move(delta)
        train.move(delta)
        police.move(delta)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                print("you have been run over! Be more careful next time.")
                print("Try again in order to reach the pond safely!")
                return
            keys = pg.key.get_pressed()
            if keys[K_s]:
                p.down(delta)
                p.setImage("./assets/frog_down.png")
                p.jumpCount += 1
            if keys[K_w]:
                p.up(delta)
                p.setImage("./assets/frog.png")
                p.jumpCount += 1
            if keys[K_a]:
                p.left(delta)
                p.setImage("./assets/frog_left.png")
                p.jumpCount += 1
            if keys[K_d]:
                p.right(delta)
                p.setImage("./assets/frog_right.png")
                p.jumpCount += 1

        counting_time = pg.time.get_ticks() - start_time
        counting_minutes = str(counting_time / 60000).zfill(2)
        counting_seconds = str((counting_time) / 1000).zfill(2)

        counting_string = "%s" % counting_seconds
        screen.fill((0, 0, 0))
        p.update(delta)
        fly.update(delta)

        if p.getWon() == True:
            paused = True
            print("Congratulations, you have crossed the road safely!")

            print("It took you " + str(counting_string) + " seconds and " + str(int(p.jumpCount / 2)) +
                  " jumps to reach the pond.")
            print("You have eaten " + str(p.flies_eaten) + " flies! giving you a -" + str(
                p.flies_eaten * 5) + " second bonus.")
            print("Your new time is: " + str((float(counting_seconds) - (p.flies_eaten * 5))))
            print("Try again to set a new record!")
            return

        if fly.eaten == True:
            p.flies_eaten += 1
            fly.eaten = False
            fly = Fly(randFly(), "./assets/fly.png")
            powerups.add(fly)
            our_go.add(fly)

        our_go.draw(screen)
        font.render_to(screen, (430, 10), "Jumps:" + str(int(p.jumpCount / 2)), WHITE, None, size=18)
        font.render_to(screen, (10, 10), "Time:" + str(counting_string), WHITE, None, size=18)
        font.render_to(screen, (3, 538), "\"Frog Jump\" By: Brandon & Dustin   "
                                          "Last Updated: 12/01/2023", WHITE, None, size=8)
        font.render_to(screen, (3, 528), "Hitting objects can set you back   "
                                         "Eat yummy flies to take -5 sec off time", WHITE, None, size=8)
        font.render_to(screen, (3, 518), "Watch out for cars!", WHITE, None, size=8)
        font.render_to(screen, (281.5, 518), "To move:W=forward A=left S=back D=right", WHITE, None, size=8)
        pg.display.flip()

def randFly():
    """ Function to get a random X/Y coordinate for the fly spawn location.

    :return: Returns an X, Y coordinate for a fly.
    """
    randX = random.randrange(25, 453, 25)
    randY = random.randrange(25, 495, 20)

    return randX, randY


main()
pg.quit()

