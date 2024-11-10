import abc

class Animal(metaclass=abc.ABC):

    def __init__(self):
        """Whatever you want here"""

    @abc.abstractclassmethod
    def communicate(self):
        """How animals communicate"""


class Bird(Animal):
    pass