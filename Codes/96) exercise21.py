# Write a function which takes list of several data types as an argument and converts the numbers in the list to strings
def conv(l):
    return [str(i) for i in l if (type(i)==int or type(i)== float)]
nums=[True, False, [1,2,3], 1, 1.0, 3]
print(conv(nums)) 