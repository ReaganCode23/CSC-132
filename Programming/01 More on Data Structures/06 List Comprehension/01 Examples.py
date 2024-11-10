

#Without List Compreshension

numbers = []

for i in range(10):
    numbers.append(i)



#with list compreshension

numbers = [i for i in range(10)
           ]

numbers = [i**2 for i in range(10) if i%2 == 0]

numbers = [(x, y) for x in range(10) for y in range(5) if x % 2 == 0]

print(numbers)

names = ["William", "Mia", "Ned", "Zach", "Alli", "Rakesh"]

first_chars = [name[0] for name in names]
print(first_chars)

[print(name[0]) for name in names if len(name) <= 4]