
#####################################################################
# author:Reagan Jose
# date:9/24/2024    
# description:Pygame 
#####################################################################
import pygame
import random
from Item import *
from Constants import *
pygame.font.init()  # Initialize the font module
font = pygame.font.SysFont("Arial", 55)


class Person(pygame.sprite.Sprite, Item):
    
    def __init__(self, name = "Player 1" , x = 200, y = 200):
        #initialize the item class
        Item.__init__(self, name, x, y)
        # Initialize the pygame.sprite.Sprite class
        pygame.sprite.Sprite.__init__(self)
        # Additional initialization for Person
        self.size = (40)
        self.color = GREY
        self.surf = pygame.Surface((self.size/3, self.size))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        self.moving_to_top = False

    def update(self, pressed_keys): 
        if pressed_keys[pygame.K_SPACE]:
            self.moving_to_top = True
        if self.moving_to_top == True:
            if self.y > 0:
                self.y -= 1
            else:
                self.moving_to_top = False
                self.resetPosition()
        if self.moving_to_top == False:
            self.resetPosition()
        
        self.rect.topleft = (self.x, self.y)
    
    def resetPosition(self):
        self.x = w.x
        self.y = w.y



    
    
    def getPosition(self):
        # Calculate the top left corner coordinates
        top_left_x = self.x - self.size // 2
        top_left_y = self.y - self.size // 2
        return (top_left_x, top_left_y)
    def __str__(self):
        return f"Person({self.name}):    size = {self.size}    x = {self.x}    y = {self.y} color = {self.color}"
    
class Wizard(pygame.sprite.Sprite, Item):
     def __init__(self):
         #initialize the item class
        Item.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = image1
        self.size = 100
        self.x = 400
        self.y = 700
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.surf = self.image
        self.rect = self.surf.get_rect(center=(self.x, self.y))


     def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.goLeft()
        if pressed_keys[K_RIGHT]:
            self.goRight()
        
        self.rect.topleft = (self.x, self.y)
    
     def getPosition(self):
        # Calculate the top left corner coordinates
        top_left_x = self.x - self.size // 2
        top_left_y = self.y - self.size // 2
        return (top_left_x, top_left_y)
     
class Spider(pygame.sprite.Sprite, Item):
     def __init__(self):
         #initialize the item class
        Item.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.spiderimage = image2
        self.x = 0
        self.y = randint(0, 400)
        self.size = 100
        self.spiderimage = pygame.transform.scale(self.spiderimage, (self.size, self.size))
        self.surf = self.spiderimage
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        self.moving_to_right = False
        self.lives = 5
        


     def update(self, pressed_keys):
            print(f"{self.rect}")
            if self.x < 1000:
                self.x += 0.5
                if self.rect.colliderect(p.rect):
                    self.resetPosition()
                    p.moving_to_top = False
                    p.resetPosition()
            else:
                self.lives -= 1
                self.resetPosition()
            self.rect.topleft = (self.x, self.y)


                
     def resetPosition(self):
         self.x = 0
         self.y = randint(0, 400)
     
         
         
        
    
     def getPosition(self):
        # Calculate the top left corner coordinates
        top_left_x = self.x - self.size // 2
        top_left_y = self.y - self.size // 2
        return (top_left_x, top_left_y)

    
    


########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
image1 = pygame.image.load('wizard.png')
image2 = pygame.image.load('spider.png')
# Create a person object
p = Person()
#Create a wizard object
w = Wizard()

s = Spider()


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
    # update themselves accordingly


    w.update(pressedKeys)
    p.update(pressedKeys)
    s.update(pressedKeys)

   


    # fill the screen with a color
    screen.fill(WHITE)

    text = font.render(f'Lives: {s.lives}', True, (255, 0, 0))
    screen.blit(text, (20, 700))
    if s.lives < 1:
        RUNNING = False

    screen.blit(p.surf, p.getPosition())
    screen.blit(w.image, w.getPosition())
    screen.blit(s.spiderimage, s.getPosition())

    pygame.display.flip()

