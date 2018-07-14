# Get input from the user
print("First Example - Simple Method")
inputFromUser = input()
print("You entered: " + inputFromUser)


# Get input from the user - 
print("\n\nSecond Example - Gives some label/instruction before the cursor") # Note \n prints new line
inputFromUser = input("Type something: ")
print("You entered: " + inputFromUser)


# Get input from the user
print("\n\nThird Example - Gives some label/instruction before the cursor")      
print("Type something: ", end="")   #  end="" - Prints without newline
inputFromUser = input()
print("You typed: " + inputFromUser)


# Get input from user until the user enters quit
print("\n\nFourth Example - Fetches input from the user until he/she enters quit")
while True:
    inputFromUser = input()

    if inputFromUser == 'quit':
        break
    else:
        print("You entered: " + inputFromUser)
    
print("You entered quit and hence program stopped looping!")