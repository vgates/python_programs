# Operations on Strings

# Use + operator to concatenate string 
s = "Ravi and " + "Anil" 
print(s) # gives the output: Ravi and Anil

x = "Ravi"
y = "Anil"
# Example 1
print( x + y ) # output: RaviAnil

# Example 2
print( x + " " + y ) # output: Ravi Anil

# Example 3
print( x + " and " + y ) # output: Ravi and Anil



# Operator * is a repetition operator for string.

# Example 1:
print( x * 3 ) #output: RaviRaviRavi

# Example 2:
print( (x + " ") * 3 ) #output: Ravi Ravi Ravi 


# Accessing Characters of a String
# x[2] means you are accessing the third character of Ravi
print(x[2]) #output: v

# z[-2] means you are accessing the second last character of the string stored in variable z
z = "Vinod"
print(z[-2]) #output: o

# z[-2] means you are accessing the last character of the string stored in variable z
z = "Vinod"
print(z[-2]) #output: o