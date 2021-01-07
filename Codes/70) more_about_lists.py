# Generating lists with range functions
num=list(range(1,11))
print(num) 

# pop() method
print(num.pop()) # it will print the item which is popped out of list
print(num)

# index method to find index of an item from the list (By default it begins searching from left!!)
print(num.index(4)) # will give index of 4 if present in the list
# print(num.index(11)) it will raise a value error since 11 is not present in the list
num.append(2)
print(num)
print(num.index(2)) # it will print the first occurence of 2 from index 0
print(num.index(2,2)) # it will print the first occurence of 2 from index 2

# passing list to a function
def negative_list(l):
    neg=[]
    for i in l:
        neg.append(-i)
    return neg
new_list=negative_list(num)
print(new_list)    