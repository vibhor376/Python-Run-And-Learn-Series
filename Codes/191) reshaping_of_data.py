# Reshaping of data means converting any dimensional array to any other dimensional array 
import numpy as np

arr=np.random.randint(1,100,20)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size) # this will give the array size! 

arr=arr.reshape(2,10) # this will convert it to 2d array with 2 rows and each row containing 10 elements (or 10 columns indirectly)
print(arr)
print(arr.ndim)
print(arr.shape)

arr=arr.reshape(20) # converting back to 1d array!
print(arr)
print(arr.ndim)
print(arr.shape)

arr=arr.reshape(2,2,5) # this will reshape it to 3d array!
print(arr)
print(arr.ndim)
print(arr.shape)

arr=arr.reshape(20)
arr=arr.reshape(2,-1) # this will automatically replace -1 with suitable value and hence it will be converted to 2d array
print(arr)
arr=arr.reshape(20)
arr=arr.reshape(-1,5) 
print(arr)

# arr=arr.reshape(-1,-1) this will give an error you have pass one of the arguments and it must divide the total elements!
# print(arr)