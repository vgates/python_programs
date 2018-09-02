# Python program to check whether a string is a palindrome or not

# A string is said to be palindrome if reverse of the string is same as string. 
# Example : abba is a palindrome
# Example : abbc is not a palindrome
# Example : malayalam is a palindrome

# Get the string input from the user and store it in the variable user_input
user_input = input("Enter your string: ") 

reversed_user_input = user_input[::-1] # reverses the string

if user_input == reversed_user_input:
    print("The string you entered is a palindrome")
else:
    print("The string you entered is not a palindrome")
