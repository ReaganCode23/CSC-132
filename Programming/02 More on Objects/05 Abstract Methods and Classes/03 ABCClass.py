from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self) -> None:
        """Animals! YES!"""
    
    @abstractmethod
    def communicate(self):
        """Implementation left to subclasses"""

class Bird(Animal):
    def __init__(self):
        """BIRD"""
    #def communicate(self):
        #pass

b = Bird()
#b.communicate()