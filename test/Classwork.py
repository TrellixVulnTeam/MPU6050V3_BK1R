
import pygame, random
# Let's import the Car Class
from car import Car

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH = 400
SCREENHEIGHT = 500

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

# Add the car to the list of objects
all_sprites_list.add(playerCar)

# Allowing the user to close the window...
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # Game Logic
    all_sprites_list.update()

    # Drawing on Screen
    screen.fill(GREEN)

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per secong e.g. 60
    clock.tick(60)

pygame.quit()