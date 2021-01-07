import numpy as np

matrix=np.array([[5,10,15],[20,25,30],[35,40,45]])
print(matrix)

print(matrix[0][1]) # this will print '10'
print(matrix[0,1]) # this will also print '10'

print(matrix[1][1]) # this will print '25'
print(matrix[1,1]) # this will also print '25'

# slicing
print(matrix[:2,:2])
''' this will print [[5 10]
                     [20 25]] '''

print(matrix[1:,1:])
''' this will print [[25 30]
                     [40 45]] '''

np.random.seed(123)
matrix2=np.random.randint(1,101,25).reshape(5,5)
print(matrix2)

print(matrix2[1:4,1:4])
''' this will print [[87 98 97]
                     [33 47 97]
                     [79 37 97]] '''

print(matrix2[2:,2:])
''' this will print [[47 97 26]
                     [37 97 81]
                     [56 68  3]] '''