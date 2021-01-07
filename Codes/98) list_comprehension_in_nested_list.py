# List comprehension in nested list

# We want the list --> [[1,2,3], [1,2,3], [1,2,3]]
# Method 1)--> without list comprehension
l=[]
for i in range(3):
    p=[]
    for j in range(1,4):
        p.append(j)
    l.append(p)
print(l)
# Method 2)--> with list comprehension
l1=[[i for i in range(1,4)] for _ in range(3)]  # Note: Here we have used '_' in for loop !!
print(l1)
