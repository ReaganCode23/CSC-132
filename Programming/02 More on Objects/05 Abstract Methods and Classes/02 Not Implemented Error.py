#Example using the NotImplementedError

class Animal:
    
    def __init__(self):
        """Whatever an animal has"""

        def communicate(self):
            raise NotImplementedError("Abstract Method communicate not implemented in subclass!")

class Bird(Animal):

    def __init__(self):
        """Whatever a bird does"""

    

b = Bird()
