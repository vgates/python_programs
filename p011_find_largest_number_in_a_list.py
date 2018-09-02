# Python program to find largest number in the list of integers

list_of_numbers = [ 4, 3, 8, 20, 11, 24, 98, 45 ]

largest = 0 # initialize the largest number as zero

# Loop through each item in the list and compare
# it with the current largest number stored in variable largest.
# If item is greater than the largest, then replace largest number
# with the item.
for num in list_of_numbers:
    if num > largest:
        largest = num

print("Largest Number in the list =", largest)
