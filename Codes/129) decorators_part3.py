from functools import wraps

def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        '''This is a wrapper function'''
        print('This is Awsome Function')
        return any_function(*args,**kwargs)
    return wrapper_function

def decorator_function2(any_function2):
    @ wraps(any_function2)
    def wrapper_function2(*args,**kwargs):
        '''This is a wrapper function'''
        print('This is Awsome Function')
        return any_function2(*args,**kwargs)
    return wrapper_function2

@ decorator_function
def add(a,b):
    '''This function will return addition of two numbers'''
    return a+b
print(add.__doc__) # it will print "This is a wrapper function"
print(add.__name__) # this will print "wrapper_function"

@ decorator_function2
def add2(a,b):
    '''This function will return addition of two numbers'''
    return a+b
print(add2.__doc__)  # it will print "This function will return addition of two numbers"
print(add2.__name__) # this will print "add2"