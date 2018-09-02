# Python program to check whether a number is prime or not.

# A positive integer which is only divisible by 1 and itself is known as a prime number.
# Example: 17 is a prime number because it is only divisible by 1 and 17
# Example: 15 is not a prime number because it is divisible by 1, 3, 5 and 15.


# get the user input and store it in the variable input_number
# int function is used to convert the user input to integer
input_number = int(input("Enter the number: "))
flag = 0

# we iterate through all numbers from 2 to input_number-1 and 
# for every number, check if it divides the input_number
# if any number (from 2 to input_number-1) divides the input_number  
# it means that the input_number is not prime hence we set a flag to 1
# Note: Modulo operator (%) returns the remainder when first operand is divided by the second.
for i in range (2, input_number):
    if input_number % i == 0:
        flag = 1
        break

# if flag is set to 1 then the input_number is not a prime number
if (flag == 0):
    print("The number {x} you entered is prime.".format(x=input_number))
else:
    print("The number {x} you entered is not prime.".format(x=input_number))