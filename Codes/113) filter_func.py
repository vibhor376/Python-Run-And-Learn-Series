# Filter function

def is_even(a):
    return a%2==0
numbers=[2,4,1,5,9,6,7,13,12]

# Our task is to create a new list which contains only even numbers from the list "numbers"
# Method 1) --> without filter function
res=[i for i in numbers if is_even(i)]
print(res)

# Method 2) --> with filter function
res2=filter(is_even,numbers)
res3=filter(lambda a:a%2==0,numbers)
res4=filter(is_even,numbers)
print(res2)
print(list(res2))
print(tuple(res3))

for i in res4:
    print(i)
for j in res4:
    print(j)
# OUTPUT will only be printed once since the filter object is iterable only once!!