# generators are iterators

# iterators vs iterables

l=[1,2,3,4] # iterable
l1=map(lambda a:a**2,l) # iterator
# We can use loops to iterate through both iterables and iterators!!

li=[1,2,3,4,5]
# memory --- [1,2,3,4,5], list, it will store as a chunk of memory!!
# memory --- (1)->(2)->(3)->(4)->(5), generators, numbers will be generated one at a time and previously generated number will be 
# deallocated after it's use, hence it is time and memory efficient!!

# If we want to use our data more than once then use lists otherwise use generators 

