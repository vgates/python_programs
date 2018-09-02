# Check whether the number entered by the user is even or odd
# Tip: A number is called even if it is divisible by 2
# Tip: A number is called odd if it is not divisible by 2

# get the user input and store it in the variable input_number
# int function is used to convert the user input to integer
input_number = int( input("Enter the number: ") )

# Modulo operator (%) returns the remainder when first operand is divided by the second.
# Use % to find the remainder when we divide the input_number by 2
# if the remainder is zero then it means that the input_number is even
if ( input_number % 2 == 0):
    print("The number", input_number, "you entered", "is even.")
else:
    print("The number", input_number, "you entered", "is odd.")
