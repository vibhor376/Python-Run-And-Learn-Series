fruits=["orange","apple","pear","Banana","Kiwi"]

# 1) pop method
fruits.pop()  # will remove the last element
print(fruits)

fruits.pop(1) # will remove the element from the list which as at index 1
print(fruits)

# 2) del method
del fruits[0] # will delete the element from the list which as at index 0
print(fruits)

# 3) remove method
fruits.remove('Banana') # removes 'Banana' from the list
print(fruits)
# if you pass such an element which is not present in the list it will show value error
# if suppose there are two same elements in the list and we pass this element in remove then first occurence of this element will be 
# removed only
f=["apples","apples"]
f.remove("apples")
print(f)