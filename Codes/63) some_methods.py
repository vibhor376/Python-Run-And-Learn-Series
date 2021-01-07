fruits=['apple','banana','orange','grapes','apple','kiwi','guava']
numbers=[10,39,24,19,1,29]
numbers_copy=[]

# 1) count method (gives the count of particular element in the list)
print(fruits.count('apple'))
print(fruits.count('orange'))
print(numbers.count(10))

# 2) sorted function
print(sorted(fruits))   # this will print fruits(list) in sorted order but will not change the fruits(list) 
print(sorted(numbers))  # this will print numbers(list) in sorted order but will not change the numbers(list) 

# 3) sort method (sort the list in increasing order)
fruits.sort()  # this will change the original one in sorted form
print(fruits)
numbers.sort() # this will change the original one in sorted form 
print(numbers)

# 4) copy method (it will copy elements of one list to another list)
numbers_copy=numbers.copy()
print(numbers_copy)

# 5) clear method (it will make our list empty)
numbers.clear()
print(numbers)

# 6) reverse method (it will reverse the order of the list)
numbers_copy.reverse()
print(numbers_copy)