import numpy as np

# 1) zeros()
arr=np.zeros(5) # this will create an array of size '5'(in this case) with all its elements as zero!
print(arr)
mat=np.zeros((2,3)) # this will create a 2d array with 2 rows and 3 columns with all its elements as zero!
print(mat)

# 2) ones()
arr1=np.ones(5) # this will create an array of size '5'(in this case) with all its elements as one!
print(arr1)
mat1=np.ones((2,3)) # this will create a 2d array with 2 rows and 3 columns with all its elements as one!
print(mat1)

# 3) eye()
mat3=np.eye(4) # this will create a 2d matrix with its diagonal elements as one and rest elements as zero!
print(mat3)
mat4=np.eye(3,4) # this will create a 2d matrix with 3 rows and 4 columns with its diagonal elements as one and rest elements as zero!
print(mat4)

# 4) diag()
arr2=np.diag([1,2,3,4]) # this will create a 2d array with diagonal elements as the elements in passed list and rest elements as zero!
print(arr2)
print(np.diag(mat3)) # this will print the diagonal elements of a matrix(2d array)

# 5) randint()
ran_arr=np.random.randint(1,15,4) # this will generate any 4 random integers between 1 and 15(not included) and then makes an array of these numbers!
print(ran_arr)

# 6) rand()
ran_arr1=np.random.rand(4) # this will generate any 4 random numbers between 0 and 1(not included) and then makes an array of these elements!
print(ran_arr1)
ran_arr2=np.random.rand(2,3) # this will generate any 4 random numbers between 0 and 1(not included) and then makes a 2d array of 2 rows and 3 columns of these elements!
print(ran_arr2)

# 7) randn()
ran_arr3=np.random.randn(4) # this will generate any 4 random numbers including both +ve and -ve numbers which have average around zero and then makes an array of thes elements!
print(ran_arr3)
print(np.mean(ran_arr3)) # this will give us the mean of elements of the array!