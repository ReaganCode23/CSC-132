


class Person:
    def __init__(self, name):
        self.name = name

    def eat():
        pass
    
    def grow():
        pass

class Adult(Person):
    def __init__(self, name, responsibilites):
        super().__init__(name)
        self.responsibilites = responsibilites

class Child(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def procrastinate():
        pass

class Programmer(Adult):
    def __init__(self, name, responsibilites):
        super().__init__(name, responsibilites)
    def gottoWork():
        pass

class Student(Adult,Child):
    def __init__(self, name, responsibilites, grades):
        Adult.__init__(self, name, responsibilites)
        Child.__init__(self, name)
        self.grades = float(grades)

