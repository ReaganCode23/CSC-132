

# Values and their squares using dictionary comprehension
values = { x : x**2 for x in range}

# Using existing data

names = ["bill", "mark", "james", "alice", "eve"]
ages = [10, 20, 30, 50, 60]

result = { names[i]: ages[i] for i in range(len(names))}

for i in range(len(names)):
    result[names[i]] = ages[i]





