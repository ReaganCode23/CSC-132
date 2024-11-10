people = [
    ["Ned", "Beef Stew"],
    ["Mia", "Crawfish"],
    ["William", "Spicy Nacho Doritos"],
    ["Josh", "Cafe Chicken Nuggets"]
]

class Person:
    
    def __init__(self, name, favorite_food):
        self.name = name
        self.favorite_food = favorite_food

    def __repr__(self):
        return f"{self.name}'s favorite food is {self.favorite_food}"
    
    @staticmethod
    def from_list(item):
        """Create a Person from a list of details about the person"""
        return Person(item[0], item[1])
    
my_data = list(map(Person.from_list, people))
print(my_data)