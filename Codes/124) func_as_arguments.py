# Functions as arguments
def square(a):
    return a**2
l=[1,2,3,4]

# Map
print(list(map(square,l)))

# Creating our own map function!
def my_map(func,l):  # here function is used as an argument
    return [func(i) for i in l]  
print(my_map(square,l))
print(my_map(lambda a:a**3,l))
