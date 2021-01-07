# We use enumerate function with for loop to track position of our item in iterable
names=["Akshat","Lekhansh","Preet"]

# Without enumerate function
pos=0
for i in names:
    print(f"{pos} --> {i}")
    pos+=1
print()
# With enumerate function
for pos, i in enumerate(names):
    print(f"{pos} --> {i}")

# Example function which takes a list and a string as arguments an returns the pos of the string in the list if present else -1
def find_pos(l,x):
    for pos,i in enumerate(l):
        if i==x:
            return pos
    return -1
print(find_pos(names,"Lekhansh"))
print(find_pos(names,"Vibhor"))
