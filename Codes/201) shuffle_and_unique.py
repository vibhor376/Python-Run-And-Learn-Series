import numpy as np

np.random.seed(123)
arr=np.random.randint(1,15,15)
print(arr)
np.random.shuffle(arr) # this will randomly shuffle the array
print(arr)
print(np.unique(arr)) # this will give the array with unique elements
print(np.unique(arr,return_index=True,return_counts=True))
# this line will print 3 things 
# 1) array with unique values
# 2) array containing the indices of each element from above array
# 3) array containing the counts of each unique element in the original array
