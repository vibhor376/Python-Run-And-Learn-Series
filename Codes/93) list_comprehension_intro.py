# With the help of list comprehension we can create list in one line

# Create a list of square numbers from 1 to 10
# Method 1)--> without list comprehension 
l=[]
for i in range(1,11):
    l.append(i**2) 
print(l)
# Method 2)--> with list comprehension
l1=[i**2 for i in range(1,11)]
print(l1)

# Create a list of negative numbers from 1 to 10
# Method 1)--> without list comprehension
neg=[]
for i in range(1,11):
    neg.append(-i)
print(neg)
# Method 2)--> with list comprehension
neg1=[-i for i in range(1,11)]
print(neg1)

# Given a list of strings and our task is to create a new list such that it contains only first character of the strings
name=["Akshat","Lekhansh","Vibhor","Yatharth"]
# Method 1)--> without list comprehension
res=[]
for i in name:
    res.append(i[0])
print(res)
# Method 2)--> with list comprehension 
res1=[i[0] for i in name]
print(res1)



