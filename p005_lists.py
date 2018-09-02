# Add even numbers to the list "evenList" between 1 to 100

#Example 1:
i=0
evenList = []
while i<101:
    evenList.append(i)
    i=i+2

print(evenList)

#Example 2:
evenList = list(range(0,101,2))
print(evenList)

# Create another list "tensList" which contains multiples of 10 from evenList
tensList = []
for a in evenList:
    if a%10 == 0:
        tensList.append(a)
print(tensList)
