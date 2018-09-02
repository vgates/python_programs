# Python program to find the sum of digits of a number

# get the user input and store it in the variable input_number
# int function is used to convert the user input to integer
input_number = int( input("Enter the number: ") )

sum = digit = 0  # initializes variable sum and digit to zero

while input_number != 0:
    digit = input_number % 10
    sum = sum + digit
    input_number = int( input_number / 10 )

print("Sum of digits =", sum)