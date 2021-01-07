import numpy as np

arr=np.array([47,1,32,190,10,19,132])

# 1) min() --> gives the minimum element in the array
print(np.min(arr))

# 2) max() --> gives the maximum element in the array
print(np.max(arr))

# 3) argmin() --> gives the index (or position) of the minimum element in the array
print(np.argmin(arr))

# 4) argmax() --> gives the index (or position) of the maximum element in the array
print(np.argmax(arr))

# 5) sqrt() --> gives the square root of each element in the array
print(np.sqrt(arr))

# 6) exp() --> gives the element with 'e'(Euler's Constant, e=2.718..) raised to the power to that element
print(np.exp(arr))

# 7) sin() --> gives the sine values corresponding to each element in the array treating them as angles (in radians)
print(np.sin(arr))

# 8) cos() --> gives the cosine values corresponding to each element in the array treating them as angles (in radians)
print(np.cos(arr))

# 9) linspace() --> gives the numbers ranging between l and r with equal intervals in between 
print(np.linspace(1,5,10)) # this will give 10 equally spaced numbers from 1 to 5

# 10) making a boolean array
arr1=np.array([-2,-1,0,1,2],dtype=bool) # this will change the datatype of the elements in the array from 'int' to 'bool'
print(arr1)

# 11) looping in arrays
for i in arr1:
    print(i)
