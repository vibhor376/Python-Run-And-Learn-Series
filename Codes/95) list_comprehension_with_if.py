# List comprehension with if statement

# Create a list which contains only even numbers from 1 to 10
# Method 1)--> without list comprehension
ev=[]
for i in range(1,11):
    if(i%2==0):
        ev.append(i)
print(ev)
# Method 2)--> with list comprehension
e=[i for i in range(1,11) if i%2==0]
print(e)

# Create a list which contains only odd numbers from 1 to 10
# Method 1)--> without list comprehension
od=[]
for i in range(1,11):
    if i%2:
        od.append(i)
print(od)
# Method 2)--> with list comprehension
o=[i for i in range(1,11) if i%2]
print(o)