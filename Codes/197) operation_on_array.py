import numpy as np

arr=np.array([1,2,3,4]) 
print(arr*2) # this will multiply each element of the array by two!
print(arr+5) # this will add 5 to each elemeny of the array!
print(arr**2) # this will square all the elements of the array!
print(arr/0) # this will not give an error but will give a warning and will fill each element of the array by 'inf'

mat=np.array([1,2,3,4]).reshape(2,2) 
print(mat*2) # this will multiply each element of the matriz by two!
print(mat+5) # this will add 5 to each elemeny of the matrix!
print(mat**2) # this will square all the elements of the matrix!
print(mat/0) # this will not give an error but will give a warning and will fill each element of the matrix by 'inf'