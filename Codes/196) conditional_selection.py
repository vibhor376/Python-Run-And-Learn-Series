import numpy as np

arr=np.arange(1,11) # this will make an array consisting of all the values from 1 to 10
print(arr)
mask=arr>5
print(mask) # this will print the array which consists of either 'True' or 'False' values according to given condition!
print(arr[mask]) # this will print only those elements of the array which satisify the above mentioned condition!
print(arr[arr%2==0]) # this will print all the even numbers in the array!
print(arr[arr==6]) 

arr[arr%2==0]=0 # assigning all the even elements in the array to zero
print(arr)