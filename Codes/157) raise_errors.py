def add(a,b):
    if type(a)==type(b):
        return a+b
    raise TypeError('Oops! You have passed a wrong set of data types!!')  # this is how we raise an error

print(add(4,5))
print(add('a','b'))
print(add('a',5))