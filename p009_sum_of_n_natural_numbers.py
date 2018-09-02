# Python program to find the sum of first n natural numbers

# The counting numbers 1, 2, 3, ... are commonly called natural numbers.

# get the user input and store it in the variable n
# int function is used to convert the user input to integer
n = int( input("Enter the value for n: ") )
sum = 0 # we will store the sum here. Hence initialize it to zero

# Example 1: Use while loop to iterate from 1 to n and add i to the variable sum
i = 1
while i <= n:
    sum = sum + i
    i = i+1
print("\nThe sum of first {0} natural numbers = {1}".format( n, sum ))


# Example 2: Using for loop and range function
sum = 0
for i in range( 1, n+1 ):
    sum = sum + i
print("\nThe sum of first {0} natural numbers = {1}".format( n, sum ))
