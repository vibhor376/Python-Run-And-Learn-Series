# make flexible fuctions
# * operator

def add(a,b):
    print(a+b)
add(4,5)
# add(4,5,7,8)  this will give an error because we have passed too many arguments

def total(*args):  # we can write anything after the * but according to convention we perfer using args after *
    print(args)
    print(type(args))
total(1,2,3,4,5,6) # the * operator will take the pass arguments and will create a tuple and we can pass as many argument as we want

def all_total(*args):
    t=0
    for i in args:
        t+=i
    return t
print(all_total(4,5))
print(all_total(4,5,7,8)) # this will now not give an error !!

