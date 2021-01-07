# lambda expressions (anonymous functions)
def add (a,b):
    return a+b
print(add(4,5))

add2=lambda a,b: a+b   # lambda function takes arguments comma separated and the body(or task) of function after colon (:)
print(add2(4,5))

# we use lambdas with built in fuctions like map, filter, reduce, etc.

mul=lambda a,b:a*b
print(mul(4,5))

# lambda functions do not have names
print(add2)
print(mul)
print(add)
