def multiply(*args):
    mul=1
    print(f"Elements in args are {args}")
    for i in args:
        mul*=i
    return mul
l=[1,2,3]
t=(1,2,3)
print(multiply(l)) # OUTPUT: [1,2,3]
print(multiply(*l)) # OUTPUT: 6 , here all the elements of the list will get unpacked
print(multiply(*t))
