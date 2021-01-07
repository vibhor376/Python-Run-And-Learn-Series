# Debugging of code is the process of finding and resolving any bugs (or problems) in the code

import pdb # python debugger module
# module --> python files containing usefull classes and functions written by developers

pdb.set_trace()  # n --> to run the current line, l --> to see the current line, q--> to quit the debugger, c--> to run code normally
name=input("Enter your name: ")
age=input("Enter your age: ")
age2=int(age)+5
print(f"Your name is {name} and your age after 5 years is {age2}")