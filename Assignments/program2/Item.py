#####################################################################
# author:Reagan Jose     
# date:   9/17/2024     
# description: Person
#####################################################################
# global Constants to restrict the maximum x and y.cord values that a person object
# can have.
MAX_X = 1000
MAX_Y = 800
import math
# A class representing a person. A person can be initialized with a
# name, as well as x and y.cord coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Item:
    def __init__(self, name = "Player1", x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y
        self.size = 500

    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        amount = 0
        for character in value:
            if character.isalpha():
                amount += 1
        
        if amount >= 2:
            self._name = value
        else:
            self._name = "Player1"

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if value < 0:
            self._x = 0
        elif value > MAX_X:
            self._x = MAX_X
        else:
            self._x = value
    

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        if value < 0:
            self._y = 0
        elif value > MAX_Y:
            self._y = MAX_Y
        else:
            self._y = value

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value > 1:
            self._size = value
        else:
            self._size = 1
    
    def goLeft(self, value = None):
        if value != None:
            self.x = self.x - value
        else:
            self.x = self.x - 1
    
    def goRight(self, value = None):
        if value != None:
            self.x = self.x + value
        else:
            self.x = self.x + 1
    
    def goUp(self, value = None):
        if value != None:
            self.y = self.y - value
        else:
            self.y = self.y - 1
    
    def goDown(self, value = None):
        if value != None:
            self.y = self.y + value
        else:
            self.y = self.y + 1
    
    def getDistance(self, other):
        return math.sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
    
    def __str__(self):
        return f"Person({self.name}):    size = {self.size}    x = {self.x}    y = {self.y}"
    

print(f"{Item.size}")