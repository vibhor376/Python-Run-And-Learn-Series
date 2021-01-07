import numpy as np

nums=[1,2,3] # list
print(nums)

nums=np.array(nums) # converting list into the numpy array
print(nums) 
print(nums.ndim) # this will print the dimension of the array
print(nums.shape) # this will give a tuple which is like (no. of rows, no. of columns)

nums1=[[1,2,3],[4,5,6]] # list of lists
print(nums1)

nums1=np.array(nums1) # converting list of lists to 2d array
print(nums1)
print(nums1.ndim)
print(nums1.shape)

nums2=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]] # complex list
print(nums2)

nums2=np.array(nums2) # creating the 3d array
print(nums2)
print(nums2.ndim)
print(nums2.shape)

print(nums.dtype) # this will give the datatype stored in nums array
print(nums1.dtype)
print(nums2.dtype)

# Note: Numpy arrays can only store the single datatype whereas list can store multiple datatypes!

nums3=[1,2,3,4.0]
nums3=np.array(nums3) # while converting all the datatypes are converted to float type
print(nums3)
print(nums3.dtype)

nums4=[1,2,3,'4',False]
nums4=np.array(nums4) # while converting all the dataypes are converted to string type
print(nums4)
print(nums4.dtype)