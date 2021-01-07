# functions practice

# Example 1) Write a function which takes a string as an argument and returns(or print) it's last character
def last_c(st):
    return st[-1]
print(last_c("Akshat"))
# but print(last_c(9)) will give you an error because it is not a string but an integer

# Example 2) Write a function which takes an integer as an argument and tell whether it is odd or even
def o_e(a):
    if a%2:
        return "Odd"
    return "Even"      # this is equivalent to putting return "Even" in else part
print(o_e(6))
print(o_e(9))

# Example 3) Reduce lines of code for Example 2)
def odd_even(a):
    return a%2==0
print(odd_even(6))  # Output will be "True" not "Even" 
print(odd_even(9))  # Output will be "False" not "Odd"

# Example 4) Function with no argument
def song():
    return "Happy Birthday!"
print(song())
