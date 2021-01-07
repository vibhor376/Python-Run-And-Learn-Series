import numpy as np

# 1) Create an array using array function
arr1=np.array([1,2,3,4])
print(arr1)

# 2) Create an array containing numbers from 20 to 40
arr2=np.array(range(20,41))
print(arr2)

# 3) Create an array which contains 10 elements and each element as 5
arr3=np.array([5 for _ in range(1,11)])
print(arr3)

# 4) Create a 1d array and convert it to 3d array
arr4=np.arange(1,10).reshape(1,3,3)
print(arr4)

# 5) Create a 2d array which contains 25 random numbers between 0 and 1
arr5=np.random.rand(25).reshape(5,-1)
print(arr5)

# 6) Create an array which contains 20 random numbers and replace every even number by -1
arr6=np.random.randint(1,25,20)
arr6[arr6%2==0]=-1
print(arr6)

# 7) Given a matrix [[5 10 15 20 25] [30 35 40 45 50] [55 60 65 70 75] [80 85 90 95 100]] and our task is to extract [[30 35 40] [55 60 65]] from it
mat1=np.array(range(5,101,5)).reshape(4,5)
print(mat1[1:3,:3])

# 8) Concatenate 2 1d arrays (note arrays or matrices should have same axis)
arr7=np.array([1,2,3,4])
arr8=np.array([5,6,7,8])
print(np.hstack((arr7,arr8)))
print(np.vstack((arr7,arr8)))

# 9) Stack two matrices both horizontally and vertically (note arrays or matrices should have same axis)
mat2=np.array([1,2,3,4]).reshape(2,2)
mat3=np.array([5,6,7,8]).reshape(2,2)
print(np.hstack((mat2,mat3)))
print(np.vstack((mat2,mat3)))
