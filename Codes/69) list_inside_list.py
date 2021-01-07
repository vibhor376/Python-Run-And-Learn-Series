# list inside list
matrix=[[1,2,3], [4,5,6], [7,8,9]] # 2D list 

# printing the elements of matrix
print(matrix[0])
print(matrix[1])
print(matrix[2])

#printing each item in the matrix separately
for sublist in matrix:
    for items in sublist:
        print(items)
print()
# accessing particular element using indices
print(matrix[0][2])
print(matrix[1][0])
print(matrix[2][1])

print(type(matrix)) # gives you the type of matrix 