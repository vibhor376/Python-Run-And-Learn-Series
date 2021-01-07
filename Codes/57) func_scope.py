#scope
y=0   
def func():
    x=10  # local variable 
    y=20  # y is not global here
    print(x,y)
def func1():
    global y  # change the global y
    y=10 # this y is global
    print(y)
    # print(x) it will give an error because scope of variable x is limited to func() means it cannot be accessed outside func()
func()
func1()