x = 5
y = "Hello, World!"

#  2. Data Types: Python supports several data types, including integers, floats, strings, booleans, lists, tuples, sets, and dictionaries.

#  Example:

# Data Types
# Integer
x = 5

# Float
y = 3.14

# String
z = "Hello, World!"

# Boolean
a = True

# List
b = [1, 2, 3, 4, 5]

# Tuple
c = (1, 2, 3, 4, 5)

# Set
d = {1, 2, 3, 4, 5}

# Dictionary
e = {"name": "John", "age": 30}

#  3. Operators: Python supports various operators, such as arithmetic operators (+, -, *, /), comparison operators (==, !=, <, >, <=, >=), logical operators (and, or, not), and more.

# Example:

# Operators
# Arithmetic Operators
a = 5 + 3    # 8
b = 5 - 3    # 2
c = 5 * 3    # 15
d = 5 / 3    # 1.6666666666666667
e = 5 % 3    # 2
f = 5 ** 3   # 125

# Comparison Operators
g = 5 == 3   # False
h = 5 != 3   # True
i = 5 < 3    # False
j = 5 > 3    # True
k = 5 <= 3   # False
l = 5 >= 3   # True

# Logical Operators
m = True and False   # False
n = True or False    # True
o = not True         # False

# 4. Control Flow Statements: Python supports several control flow statements, such as if-else statements, for loops, while loops, and more.

# Example:

# Control Flow Statements
# if-else statement
a = 5
if a > 3:
    print("a is greater than 3")
else:
    print("a is less than or equal to 3")

# for loop
b = [1, 2, 3, 4, 5]
for i in b:
    print(i)

# while loop
c = 1
while c <= 5:
    print(c)
    c += 1

# 5. Functions: In Python, you can define your own functions to perform specific tasks. You can pass arguments to functions and return values from functions.

# Example:

# Functions
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  



# to draw a line we use turtle 

import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to the starting position
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw a line
t.forward(200)

# Exit the program when the user clicks the window
turtle.exitonclick()
