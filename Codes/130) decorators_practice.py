from functools import wraps
def function_support(any_function):
    @ wraps(any_function)
    def wrapper_function(*args,**kwargs):
        '''This is a Wrapper function'''
        print(f'You are calling {any_function.__name__} function')
        print(f'{any_function.__doc__}')
        return any_function(*args,*kwargs)
    return wrapper_function

@ function_support
def add(a,b):
    '''This Function takes 2 arguments and return their sum'''
    return a+b
print(add(4,5))