# Write a program which takes many lists and gives the average of the matching index elements of the lists
# Example --> [1,2,5], [6,4,3], [9,8,7]  average= [(1+6+9)/3 , (2+4+8)/3, (5+3+7)/3]
# Note: Try to use lambda function (Bonus)
l1=[1,2,5]
l2=[6,4,3]
l3=[9,8,7]

# Method 1)
res=list(map(lambda l:sum(l)/len(l),list(zip(l1,l2,l3))))
print(res)

# Method 2)
res2=lambda *args: [sum(p)/len(p) for p in zip(*args)]
print(res2(l1,l2,l3))
