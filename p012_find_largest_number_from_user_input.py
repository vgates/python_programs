# Python program to find largest number from the inputs 
# entered by the user.

# First get the user input to a list

list_of_numbers = [] # initializing empty list

print("Type user number and click enter. If you are done type q.\n")

# Convert the input to int and append it to the list_of_numbers
# until user enters q
while True:    
    user_input = input() # store the user input to user_input

    if user_input == 'q':
        break
    else:
        list_of_numbers.append( int( user_input ) ) # append input to the list

largest = 0 # initialize the largest number as zero

# Loop through each item in the list and compare
# it with the current largest number stored in variable largest.
# If item is greater than the largest, then replace largest number
# with the item.
for num in list_of_numbers:
    if num > largest:
        largest = num

print("Largest Number in the list =", largest)
