name="Akshat"
print(len(name)) # len() is a function which gives us the length of a given string

# user defined function example
def add_two(a,b):
    return a+b   # return a+b means that this function will return the sum of a and b

total=add_two(5,4)
print(total)

x,y=input("Enter any two numbers: ").split()
x=int(x)
y=int(y)
print(add_two(x,y))

g,h=input("Enter first name and last name: ").split()
print(f"Your full name is {add_two(g,h)}")