# List Comprehension with if else statement
nums=list(range(1,11))

# Print a list which prints -n when n is odd and 2*n when n is even where n belongs to the original list
# Method 1)--> without list comprehension
res=[]
for i in nums:
    if i%2==0:
        res.append(i*2)
    else:
        res.append(-i)
print(res)
# Method 2)--> with list comprehension
res1=[i*2 if i%2==0 else -i for i in nums]
print(res1)