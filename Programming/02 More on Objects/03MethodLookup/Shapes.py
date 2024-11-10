

class Shape:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def draw(self):
        for _ in range(self.width):
            print("* " * self.length)

class Rectangle(Shape):

    def __init__(self, length, width) -> None:
        super().__init__(length, width)\
        #Shape.__init__(self, length, width)

class Square(Shape):

    def __init__(self, length) -> None:
        super().__init__(length, length)

class Triangle(Shape):
    #This is specifically a right isosceles triangle
    def __init__(self, leg_length) -> None:
        super().__init__(leg_length, leg_length)
    
    def draw(self):
        for i in range(self.width):
            print("* " * (self.width - i))

print("Rectangle\n")
r = Rectangle(5,3)
r.draw()

print("Square\n")
s = Square(4)
s.draw()

print("Triangle\n")
t = Triangle(4)
t.draw()

