# Ask user to input until he/she enters valid input
# For example: Get age from the user. The input should be always an integer value
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Invalid input provided. Type your age")
        continue
    else:
        # since valid we exit from the loop
        break
if age >= 18: 
    print("You can apply for driving license!")
else:
    print("You are not eligible to apply for driving license.")