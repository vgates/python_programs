# Python program to find factorial of a number

# Factorial of a number n is the multiplication of all 
# integers smaller than or equal to n.
# Example: Factorial of 5 is 5x4x3x2x1 which is 120.

# Here we define a function for calculating the factorial.
# Note: Functions are the re-usable pieces of code which 
# helps us to organize structure of the code.
# Python uses def keyword to start a function.
# Refer https://thepythonguru.com/python-functions/

def factorial( input_number ):
    temp_factorial = 1
    for i in range(1, input_number + 1):
        temp_factorial = temp_factorial * i
    return temp_factorial

# get the user input and store it in the variable input_number
# int function is used to convert the user input to integer
input_number = int( input("Enter the number: ") )

# call the factorial function which we have defined 
calculated_factorial = factorial( input_number )

# Print
print("Factorial of {0} = {1}".format( input_number, calculated_factorial) )
