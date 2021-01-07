# Write a function which takes three numbers as an argument and returns the greatest among them
def great3(a,b,c):
    if a>b:
        if a>c:
            return a
        return c
    else:
        if b>c:
            return b
        return c
x,y,z=input("Enter any three numbers: ").split()
print(f"Greatest number is: {great3(int(x),int(y),int(z))}")