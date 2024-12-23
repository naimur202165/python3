import random

# List of all imported modules
imported_modules = ["random"]

# Print statement
print("hello world")

# Conditional statements
if 5 > 2:
    print("true")
    print("naimur rahman")

# Working with variables
x = 10
y = "Naimur Rahman Durjoy"
print(x, y)

# Working with functions
h = "naimur rahman"
def func():
    print("I am " + h)

func()

def rony():
    global x
    x = "This is a global variable"

rony()

# Working with numbers
num1 = 1
num2 = 3
com = 1j
print(num1, num2, com)
print(random.randrange(1, 10))

# String methods
name = "naimurahman"
print(name.lower())
print(name.strip())
# print(name.count())

# Working with lists
mylist = ["naimur", "basic", "ridoy"]
print(mylist)
print(len(mylist))
print(type(mylist))
print(random.randrange(1, 10))

# List methods
mylist.append("Simul")
print(mylist)

# Looping through lists
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in fruits:
    print(x)

# Nested loops
for x in fruits:
    for color in colors:
        print(f"{x} is {color}")

# Working with sets
myset = {"naimur"}

# Example of nested for loops
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
# ...existing code...


