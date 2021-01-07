def decorator_function(any_function):
    def wrapper_function():
        print('This is Awsome Function')
        any_function()
    return wrapper_function

def decorator_function2(any_function2):
    def wrapper_function2(*args,**kwargs):
        print('This is Awsome Function')
        any_function2(*args,**kwargs)
    return wrapper_function2

def decorator_function3(any_function3):
    def wrapper_function3(*args,**kwargs):
        print('This is Awsome Function')
        return any_function3(*args,**kwargs)
    return wrapper_function3

@ decorator_function
def func():
    print('This is a Function')
func()

@ decorator_function
def func2(a):
    print(f"This is a Function with argument {a}")
# func2() this will give an error because wrapper function does not take any argument

# To fix this issue we will provide *args and **kwargs to both wrapper_function as well as any_function!!

@ decorator_function2
def func3():
    print('This is a Function')
func3()

@ decorator_function2
def func4(a):
    print(f'This is a Function with argument {a}') 
func4(3)

@ decorator_function2
def add(a,b):
    return a+b
print(add(4,5)) # it will print 'None' instead of its calculated value

# to fix this we return our any_function()!!

@ decorator_function3
def add1(a,b):
    return a+b
print(add1(4,5))

@ decorator_function3
def func5():
    print('This is a Function')
func5()

@ decorator_function3
def func6(a):
    print(f'This is a Function with argument {a}') 
func6(7)