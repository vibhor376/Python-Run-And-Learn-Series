import numpy as np

np.random.seed(123)
matrix1=np.random.randint(1,20,9).reshape(3,3)
matrix2=np.random.randint(20,40,9).reshape(3,3)

print(matrix1)
print(matrix2)

# Horizontal Stacking --> it means to concatenate two matrices horizontally or placing one matrix on right of the other matrix
print(np.hstack((matrix1,matrix2))) # notice that it takes arguments in tuple format

# Vertical Stacking --> it means to concatenate two matrices vertically or placing one matrix on bottom of the other matrix
print(np.vstack((matrix1,matrix2))) # notice that it takes arguments in tuple format

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.hstack((arr1,arr2))) 
print(np.vstack((arr1,arr2))) # this will convert into a 2d array