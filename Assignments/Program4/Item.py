import math
WIDTH = 1000
HEIGHT = 800

class Item:
    def __init__(self, name="Player1", x=500, y=400):
        self.name = name
        self._x = x
        self._y = y
        self.size = 50  # Adjust the size as needed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        amount = sum(1 for char in value if char.isalpha())
        self._name = value if amount >= 2 else "Player1"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = max(0, min(value, WIDTH))

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = max(0, min(value, HEIGHT))

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = max(1, value)

    def goLeft(self, value=1):
        self.x -= value

    def goRight(self, value=1):
        self.x += value

    def goUp(self, value=1):
        self.y -= value

    def goDown(self, value=1):
        self.y += value

    def getDistance(self, other):
        return math.sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))

    def __str__(self):
        return f"Person({self.name}): size = {self.size}, x = {self.x}, y = {self.y}"
