from functools import reduce

values = [1, 2, 3, 4, 5]

def multiply(a,b):
    print(f"a = {a} b = {b}")
    return a * b

product = reduce(multiply, values)
print(product)
