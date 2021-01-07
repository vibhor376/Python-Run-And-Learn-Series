# *args with normal parameters

def multiply(nums,*args):
    mul=1
    print(f"Elements in args are {args} and nums is {nums}")
    for i in args:
        mul*=i
    return mul

print(multiply(2,2,3))  # nums will be equal to 2 and args will be (2,3)
print(multiply(4,5,7,3)) # nums will be equal to 4 and args will be (5,7,3)
print(multiply(2)) # nums will be equal to 2 and args will be ()
# print(multiply()) this will give an error because we have give some value for nums

# NOTE: The normal parameters should only be declared before *args and not after it, if you do so you will get an error!!
