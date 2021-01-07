# Iterators vs iterables

numbers=[1,2,3,4] # list,tuple,strings,etc. --- iterable
square=map(lambda a:a**2,numbers) # iterator

for i in numbers:
    print(i)

# working of for loop
# 1) it will call the iter() function
# 2) iter(numbers)--> iterator
# 3) next(iter(numbers)) --> will give next iterator(or it will move one position ahead in numbers) and this process continues till 
# condition is true

number_iter=iter(numbers)  # number_iter is iterator
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))        
print(next(number_iter))

# so this way for loop internally works!!

print(square) # it is a map object iterator
print(next(square))
print(next(square))
print(next(square))
print(next(square))