# matrix with 3 rows and 3 columns
X = [
    [5,7,3],
    [4,5,2],
    [1,6,2]
    ]

# matrix with 3 rows and 3 columns
Y = [
    [9,4,1],
    [6,9,3],
    [9,5,4]
    ]

# final matrix initialized with 0
R = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

# add each element of matrix X and Y and store it in R
for i in range(len(X)):
   for j in range(len(X[0])):
       R[i][j] = X[i][j] + Y[i][j]

for r in R:
   print(r)