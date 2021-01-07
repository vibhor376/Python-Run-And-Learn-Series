# return vs print
def add_three(a,b,c):
    return a+b+c
add_three(5,5,5)  # this will just evaluate the sum and not print it
print(add_three(5,5,5))  # this will print the result as well

# now lets see an another case

def adder(a,b,c):
    print(a+b+c)
adder(5,5,5) # now this will print our result