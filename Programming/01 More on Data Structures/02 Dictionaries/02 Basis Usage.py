#defining the dictionary
a_person = {
    "first": "Josh",
    "last": "Coriell",
    "food": "Cafe Chicken Nuggests",
}

#accessing values
print(a_person["first"])
a_person["food"]
#a_person["color"]
#a_person["fave_color"]

#a "safe" way to access values

#a "safe" way to access

fave_color = a_person.get("fave_color", "Blue")
print(fave_color)

# reassign or assign values after definition
a_person["fave_food"] = "tacos"
a_person["fave color"]= "blue"