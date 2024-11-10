#we have a function
names = ["Aaron", 
         "Alicia", 
         "Ronaldo", 
         "Messi", 
         "Darwin", 
         "Nigil", 
         "Thornberry"]
#we have a function that returns True/False
def starts_with_a(name: str) -> bool:
    if name[0] =='A':
        return True
    else:
        return False
    
#apply filter
a_names = filter(starts_with_a, names)
print(list(a_names))

#Lambda Functions
#aka Anonymous

say_hello = lambda: print("hello")
say_hello()

#with a parameter
x = lambda name: print(f"hello, {name}")
y = lambda name, age: print(f"hi, {name}. You are {age}.")

x("Alberto")
y("Alberto", 344)

#filter with lambda function
a_names = filter(lambda name: name[0] == 'A', names)

print(list(a_names))
