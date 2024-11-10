# let's say this info was sent over an HTTP Request

users = [
    {"username": "Ben10", "age": 10},
    {"username": "Ronaldo", "age": 39},
    {"username": "Messi", "age": 37},
    {"username": "Bill", "age": 20},
]

def age_is_even(user: dict) -> bool:
    if user["age"] % 2 == 0:
        return True
    else:
        return False
    

people_with_even_ages = list(filter(age_is_even, users))
print(people_with_even_ages)

people_with_even_ages = list(filter(lambda user: user["age"] % 2 == 0, users))