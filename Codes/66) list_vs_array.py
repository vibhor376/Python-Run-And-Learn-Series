# list vs array

# c, c++, java
# array int,string,..(only single data type can be used at a time)

# list -- store any data / flexible

# python array module -- fix data type

# numpy arrays in python -- binding with C libraries (used mostly for data science)

# Javascript array = lists in python   

import time,numpy

t1=time.time()
l=[i**2 for i in range(1,10000000)]
t2=time.time()
print(t2-t1)

t3=time.time()
arr=numpy.arange(1,10000000)**2
t4=time.time()
print(t4-t3)