# In this problem we will be given two numbers and we need define a function which tells which one of them is greater!
def great(a,b):
    if a>b:
        return a
    elif a==b:
        return "Both are Equal"
    return b
x,y=input("Enter any two numbers: ").split()
x=int(x)
y=int(y)
print(great(x,y))