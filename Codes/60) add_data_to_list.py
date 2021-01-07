fruits=["mango","orange"]
f=["apple","banana"]
f1=["mango","orange","grapes"]

# 1) insert
fruits.insert(1,"grapes") # it will insert 'grapes' at index 1
print(fruits)

# 2) concatination of lists
res=fruits+f # concatenating both the lists
print(res)

# 3) extend method
fruits.extend(f)
print(fruits)

# 4) append method
f1.append(f)
print(f1)
