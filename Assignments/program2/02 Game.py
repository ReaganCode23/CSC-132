#####################################################################
# author:Reagan Jose
# date:9/24/2024    
# description:Pygame 
#####################################################################
import pygame
import random
from Item import *
from Constants import *

class Person(pygame.sprite.Sprite, Item):
    
    def __init__(self, name = "Player 1" , x = 0, y = 0):
        #initialize the item class
        Item.__init__(self, name, x, y)
        # Initialize the pygame.sprite.Sprite class
        pygame.sprite.Sprite.__init__(self)
        # Additional initialization for Person
        self.color = [111, 222, 222]
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
    
    def setColor(self):
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.surf.fill(self.color)
    
    def setSize(self):
        self.size = random.randint(10,100)
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill(self.color)


    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.goUp()
        if pressed_keys[K_DOWN]:
            self.goDown()
        if pressed_keys[K_LEFT]:
            self.goLeft()
        if pressed_keys[K_RIGHT]:
            self.goRight()
        if pressed_keys[K_SPACE]:
            self.setColor()
            self.setSize()

    def setRandomPosition(self):
        self.x = random.randint(0,1000)
        self.y = random.randint(0, 800)
    
    def getPosition(self):
        # Calculate the top left corner coordinates
        top_left_x = self.x - self.size // 2
        top_left_y = self.y - self.size // 2
        return (top_left_x, top_left_y)
    def __str__(self):
        return f"Person({self.name}):    size = {self.size}    x = {self.x}    y = {self.y} color = {self.color}"




print(f"{Item.size}")



########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

