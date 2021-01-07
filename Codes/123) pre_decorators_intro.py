def square(a):
    return a**2
s=square(int(input("Enter a number: ")))
print(s)
s1=square  # now s1 will also behave as square function!!
print(s1(int(input("Enter second number: "))))
print(s1 is square) # OUTPUT: True, because s1 points to square
print(s1.__name__) # OUTPUT: square, because s1 points to square