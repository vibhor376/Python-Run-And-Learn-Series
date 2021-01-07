# Functions returning two values
def operations(a,b):
    add=a+b
    multiply=a*b
    return add,multiply
a,b=input("Enter two numbers ").split()
res=operations(int(a),int(b)) # res will be a tuple type!!
add,mul=operations(int(a),int(b))
print(type(res))
print(res)
print(add)
print(mul)