# Decorators --> Enhances the functionality of the other functions
# @ is used for decorators
def decorator_function(any_function):
    def wrapper_function():
        print('This is Awsome function')
        any_function()
    return wrapper_function

# with using @ 
@ decorator_function
def func1():
    print('This is Function 1')
func1()

@ decorator_function
def func2():
    print('This is Function 2')
func2()

# without using @
def func3():
    print('This is Function 3')

def func4():
    print('This is Function 4')

func3=decorator_function(func3)
func4=decorator_function(func4)
func3()
func4()
