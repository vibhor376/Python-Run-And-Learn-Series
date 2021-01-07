l1=[1,3,5,7]
l2=[2,4,6,8]

l=[(1,2),(3,4),(5,6),(7,8)]

# Our task is to convert l into l1 and l2
# We will use * operator with zip
l3,l4=list(zip(*l))
print(list(l3))
print(list(l4))

# Our task is to create a new list using l1 and such that new list contains elements in sorted order
res=[]
for pair in zip(l1,l2):
    res.append(min(pair))
    res.append(max(pair))

print(res)