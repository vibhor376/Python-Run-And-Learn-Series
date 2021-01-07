import numpy as np

arr=np.array([5,10,15,20,25,30])

sliced_array=arr[2:5]
print(sliced_array)
sliced_array[:]=0 # you can change/update the values in the array!!
print(sliced_array)
print(arr) # the changes made in the 'sliced_array' will also be reflected in 'arr', this is because 'sliced_array' is just a "View" of 'arr' not the spearate copy of it!!

sliced_array2=arr[:2].copy() # this will make the copy from the arr
sliced_array2[:]=0
print(sliced_array2)
print(arr) # the changes made in the 'sliced_array2' will not be refelcted in 'arr' now !