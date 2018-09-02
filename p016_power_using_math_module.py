# Find x raised to the power y using math module in Python

# math is an inbuilt python module
# Python module is a normal python file which can store 
# function, variable, classes, constants etc.

# Reference link all the functions available in math 
# module https://docs.python.org/3/library/math.html

import math # imports math module

# get the user input x and y
# int function is used to convert the user input to integer
x = int( input("Enter x: ") )
y = int( input("Enter y: ") )

# Calculate the power using the function pow() defined in the 
# math module we imported.
result = math.pow(x, y)

print("{x} raised to the power {y} =".format(x=x,y=y), result)