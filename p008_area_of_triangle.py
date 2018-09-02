# Python program to find area of the triangle

# Tip: Formulae to find the area of a triangle is given below:
# Area = sqrt( s*(s-a)*(s-b)*(s-c) )
# where a, b and c are length of the sides of triangle and s = (a+b+c)/2
# s is the semiperimeter of the triangle

# get the inputs a, b, c from the user
# float function is used to convert the user input to float type
a = float( input("Length of side a: ") )
b = float( input("Length of side b: ") )
c = float( input("Length of side c: ") )

# Calculate s
s = ( a + b + c ) / 2

# Calculate area
area = ( s * (s-a) * (s-b) * (s-c) ) ** 0.5

# Print Area
print("\nArea of the triangle =", area)
