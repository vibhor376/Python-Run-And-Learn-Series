import numpy as np

arr= np.array([i for i in range(5,26,5)])
print(arr)

# Note: Index Positioning starts from 0 in numpy arrays
print(arr[0])
print(arr[3])
print(arr[-1]) # here we can use -ve indexing also 
print(arr[-3])

# slicing
print(arr[1:3]) # this will print the array elements starting from index '1' and ending at index '2', '3' is not included!
print(arr[::-1]) # this will print the array in reverse format
print(arr[:]) # this will print the whole array