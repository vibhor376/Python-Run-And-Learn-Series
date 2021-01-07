# Map Function

l=[1,2,3,4]
print()
def square(a):
    return a**2

# Our target is to get a list with each elements raise to the power of 2 using square function

# Without map function(using list comprehension)
l1=[square(i) for i in l]
print(l1)

# With map function
l2=map(square,l)
print(l2)
print(list(l2))
l3=tuple(map(lambda a:a**2,l))
print(l3)

# Without map function(normal method)
l4=[]
for i in l:
    l4.append(square(i))
print(l4)

# Given a list of strings and we have to find length of each element in the list
names=['Akshat','Lekhansh','Preet']
length=map(len,names)
for i in length:
    print(i)
for j in length:
    print(j)
# OUTPUT will be displayed only one time even if we have run the loops 2 times since we can iterate through map object only once!!
length2=list(map(len,names))
print(length2)