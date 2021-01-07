import numpy as np

np.random.seed(123)
mat=np.random.randint(1,11,9).reshape(3,3)
print(mat)
print(np.sum(mat)) # this will print the sum of all the elements in the given matrix! 
print(mat.sum()) # this will also print the sum of all the elements in the given matrix!
print(np.min(mat)) # gives the minimum element in the matrix!
print(np.max(mat)) # gives the maximum element in the matrix!
print(np.min(mat,axis=1)) # this will give minimum element corresponding to each row in the form of array
print(np.max(mat,axis=0)) # this will give maximum element corresponding to each column in the form of array
print(np.sum(mat,axis=1)) # this will give the sum of elemenets corresponding to each row in the form of array
print(np.sum(mat,axis=0)) # this will give the sum of elemenets corresponding to each column in the form of array
print(np.cumsum(mat)) # this will give the cumilative sum in the form of array
print(np.cumsum(mat,axis=0)) # this will give the column-wise cumilative sum in the form of array
print(np.cumsum(mat,axis=1)) # this will give the row-wise cumilative sum in the form of array
print(np.prod(mat,axis=0)) # this will give the column-wise product in the form of array
print(np.prod(mat,axis=1)) # this will give the row-wise product in the form of array