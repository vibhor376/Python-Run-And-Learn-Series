import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
print(arr1+arr2) # it will add those elements which have the same index and then print them
print(arr1*arr2) # it will multiply those elements which have the same index and then print them
print(arr1/arr2) # it will divide those elements which have the same index and then print them
print(arr1**arr2) # it will raise the power of those elements which have the same index and then print them
print(arr1*arr1)

# NOTE: The above operations will only be performed if the shape of the given two or more arrays are same!!

np.random.seed(123)
mat=np.random.randint(1,12,9).reshape(3,3)
mat1=np.random.randint(5,15,9).reshape(3,3)
print(mat)
print(mat1)
print(mat+mat1) # this will add the corresponding elements of the two matrices
print(mat-mat1) # this will subtract the corresponding elements of the two matrices
print(mat*mat1) # this will multiply the corresponding elements of the two matrices but this type of multiplication is not there in linear algebra!!
print(mat.dot(mat1)) # this will print the dot product or multiplication according to linear algebra!!

# NOTE: The above operations will only be performed if the shape of the given two or more matrices are same!!
