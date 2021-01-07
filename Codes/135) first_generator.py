# Create your first generator with generator function
# Method 1) --> generator function
# Method 2) --> generator comprehension

# Write a function which takes an integer as an argument and prints all the numbers from 1 to n

def nums(n):
    for i in range(1,n+1):
        print(i)
nums(5)

def nums1(n):
    for i in range(1,n+1):
        yield(i)   # or yield i      # this statement makes nums1 a generator!!
print(nums1(5)) # now nums1 has become a generator!!

for i in nums1(5):  # you can iterate through nums1(5) as it is an iterator!!
    print(i)
print("printing numbers..")
numbers=nums1(5)
for i in numbers:
    print(i)

for i in numbers:
    print(i)
# numbers will be printed only once!!

print("printing numbers which is converted to list...")
numbers1=list(nums1(5))
for i in numbers1:
    print(i)

for i in numbers1:
    print(i)
# numbers2 will printed twice as it is list now