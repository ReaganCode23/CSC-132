# 03 Inheritance.py

class Person:
    def __init__(self, name) -> None:     #type hint
        self.name = name
    
    def __str__(self) -> str:
        return self.name
    
class Student:
    def __init__(self) -> None:
        pass
    

class Bill(Person, Student):  #Bill is a Person (declaring the inheritnce relationship)
    
    def __init__(self):
        super().__init__("Bill")   #call constructor of super classs to attach properties
    
    def __str__(self) -> str:
        return f"Bill object: {super().__str__()}"
    

b = Bill()
print(b) #If Bill does not have a string function, it will go the string fuction of the parent function *method lookup*

