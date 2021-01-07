# Decorators with arguments
from functools import wraps
def only_data_types_allowed(data_type):
    def decorator(function):
        @ wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(i)==data_type for i in args]):
                return function(*args,**kwargs)
            print("Invalid arguments!")
        return wrapper
    return decorator

@ only_data_types_allowed(str) # this will allow only 'string' data_type
def string_join(*args):
    res=""
    for i in args:
        res+=i
    return res

print(string_join('Akshat','Bhatnagar'))
print(string_join('Akshat',1)) # Since we have to ensure that all the passed arguments should have 'string' data type
print(string_join('I','Am','Great'))

@ only_data_types_allowed(int) # this will allow only 'int' data_type
def add(*args):
    return sum(args)
print(add(4,5,6,2))
print(add('Akshat',1)) # Since we have to ensure that all the passed arguments should have 'int' data type