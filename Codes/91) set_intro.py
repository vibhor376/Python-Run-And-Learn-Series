# set data type
# set is unordered collection of unique items
s={1,2,3,4,2,4,1}  # this is the syntax for creating a set
print(s)  # set will contain only unique items no matter how many times you insert same value to set it will consider it only one time
# unordered means you cannot use indexing to access any particular element in the set
r={1,2,3.0,'String',1.0} # notice that it treats 1.0 and 1 as same element 
print(r)

# Note: You Cannot store lists or dictionaries in the set!!

# remove duplicate 
l=[1,2,3,4,4,4,5,5,5,5,5,2,6,6,6,7,7]
st=list(set(l))  # first l will convert into set and set will remove all the duplicates and then this set is converted back into list
print(st) # it will print only unique values 

# insert in set
s2={1,2,3}
s2.add(4)
print(s2)
s2.add(3) # adding duplicate item to the set won't effect it
print(s2)

# remove an element for the set
s2.remove(4)
print(s2)
# if you try to remove an element which is not present in the set then it will give an error
s2.discard(4) # it will not give error on passing the element which is not present in the set
print(s2)
s2.discard(3)
print(s2)

# clear method
s2.clear() # it will clear all the elements from the set and make it empty!
print(s2)

# copy method
s3=s.copy()
print(s3)
print(s)
print(s3 is s) # OUTPUT: False
