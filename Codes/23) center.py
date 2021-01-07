# center method
name="Akshat"
print(name.center(10))  # Output: **Akshat**  here star(*) denotes spaces
print(name.center(10).replace(" ","*")) # Output: **Akshat**
print(name.center(12,"*")) # Output: ***Akshat***
print(name.center(7,"*"))  # Output: *Akshat

#Example program
n1=input("Enter Your Name ")
print(n1.center(len(n1)+8,"*"))