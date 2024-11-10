a_person = {
    "first": "Josh",
    "last": "Coriell",
    "food": "Cafe Chicken Nuggests",


}




for key in a_person:
    print(key)

print()


print()
#iterate over values
for value in a_person.values():
    print(value)


#interate over keys to get values
for key in a_person:
    print(a_person[key])
print()

#iterating over keys and values

for key, value in a_person.items():
    print(key, value)