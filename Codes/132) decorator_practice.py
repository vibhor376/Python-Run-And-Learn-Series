from functools import wraps
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add_all(1,2,3,4,5))
# print(add_all(1,2,3,4,[5,6,7])) this will give an error so to resolve such problem we will use a decorator which gives an error
# message to user if any value other than int or float is passed otherwise returns their sum

def numbers_only_allowed(function):
    @ wraps(function)
    def wrapper(*args,**kwargs):
        if all([True if(type(i)==int or type(i)==float) else False for i in args]):
           return function(*args,**kwargs)
        print("Wrong Arguments were passed") # if you write return statement instead of print then 'None' will not be there in output
    return wrapper

@ numbers_only_allowed
def add_all1(*args):
    total=0
    for i in args:
        total+=i
    return total

print(add_all1(1,2,3,4,5))
print(add_all1(1,2,3,4,[5,6,7]))
print(add_all1(1,2,3,4,'Akshat'))
