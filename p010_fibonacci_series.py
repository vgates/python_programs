# Python program to print first n Fibonacci Numbers.

# The Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# The sequence is characterized by the fact that every number after the 
# first two is the sum of the two preceding ones.

# get the user input and store it in the variable n
# int function is used to convert the user input to integer
n = int( input("Enter the value for n: ") )


a = 0   # first fibonacci number
b = 1   # second fibonacci number
sum = 0 # sum of the two preceding ones

# Print first number, second number.
# Print should not end with a new line, instead it ends with a space
# since we need to print the sequence in the same line. Hence provided with end = " "
print( a, b, end = " ")

for i in range( 2, n ):
    sum = a + b # add previous two numbers
    a = b
    b = sum 
    print(sum , end=" ")


print("") # just to print a new line when the sequence is complete