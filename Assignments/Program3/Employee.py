#####################################################################
# author: Reagan Jose    
# date:         
# description:  
#####################################################################

# import the abc library to make abstract classes
from abc import ABC, abstractmethod

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################

class Employee:
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = email = None
        self.position = position = None

    
    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, value):
        value[0].upper()
        value = value.replace(" ", "")
        value = [i.lower() for i in value if i != value[0]]
        self._lastname = value
        return self._lastname
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, value):
        value[0].upper()
        value = value.replace(" ", "")
        value = [i.lower() for i in value if i != value[0]]
        self._firstname = value
        return self._firstname

    @property
    def pay(self):
        return self._pay
    
    @pay.setter
    def pay(self, value):
        if isinstance(value, int) != True:
            return "Not true"
        
        if value < 0:
            value = 20000
            return value
        else:
            return value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if value == None:
            return "invalid email"

        if "@latech.edu" in value:
            return value
        
        else:
            return "invalid email"
    

    @abstractmethod
    def applyRaise(self, rate):
        """Apply raise"""
        
    def create_email(self):
        return (self.firstname + "." +self.lastname + "@latech.edu").lower()
    
    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname} ({self.email})"





        

######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################
class Faculty(Employee):
    def __init__(self, firstname, lastname, position) -> None:
        super().__init__(firstname, lastname, position)
        self.pay = 50,000
    def applyRaise(self, rate):
        if rate > 0:
            self.pay * rate
    def __str__(self):
        return super().__self__() + f"- {self.position}"
        
######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################
class Staff(Employee):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.pay = 40000

    def applyRaise(self, rate):
        if rate > 0:
            self.pay += rate

