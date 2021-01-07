# Function inside a Function
def great(a,b):
    if a>b:
        return a
    return b
def great3(a,b,c):     # this function will return greatest number among the given three numbers
    return great(a,great(b,c))  # function calling inside function!!
x,y,z=input("Enter any three numbers: ").split()
print(f"Greatest Number among three numbers is: {great3(int(x),int(y),int(z))}") 
