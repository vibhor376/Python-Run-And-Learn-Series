# All, any functions
numbers1=[2,4,6,8,10]
numbers2=[1,2,3,4,5,6]

# Our task is to create a list which has element 'True' if element is even else 'False'
even1=[i%2==0 for i in numbers1]
print(even1)
even2=[i%2==0 for i in numbers2]
print(even2)

# all function
# if all values are true then only it will print 'True' else it will print 'False'
print(all(even1))
print(all(even2))

# any function
# if atleast one value is true it will print 'True' else it will print 'False'
print(any(even1))
print(any(even2))
l=[False,False]
print(any(l))