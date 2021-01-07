import numpy as np

np.random.seed(12) # this is done in order to fix the random number generated every time
arr=np.random.randint(1,101,10)
print(arr)
print(arr.size) # this will give the size of an array