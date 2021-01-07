# Write a function which takes an integer and a list or tuple as an argument(Use parameter * args) and returns the list or tuple 
# which contans elements raise to the power of passed integer
# Example  n=3 and l=[1,2,3]  so output will be [1,8,27] 
# If user did not pass any list or tuple then print the message that you have not given any list or tuple else return the list

def res(nums,*args):
    if args:  # this condition will check whether args is empty or not
        print([i**nums for i in args])
    else:
        print("Hey!, You didn't pass the args")

l=[4,6,2,8,3]
t=(2,5,6,8)
res(3,*l)
res(2,*t)
res(4,)

