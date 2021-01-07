# Function returning function (closure or first class functions) practice

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power
cube=to_power(3)  # cube will be the calc_power function with x=3
square=to_power(2) # square will be the calc_power function with x=2
print(cube(int(input("Enter first number: "))))
print(square(int(input("Enter second number: "))))