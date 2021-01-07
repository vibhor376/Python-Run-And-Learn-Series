# Write a funtion which contains many values as arguments and return sum of of them only if all of them are either int or float 

def my_sum(*args):
    if all([type(i)== int or type(i)== float for i in args]):
        total=0
        for i in args:
            total+=i
        return total
    else:
        return "WRONG INPUT!"

print(my_sum(1,2,3,6.7,9.8,[1,2,3],"Akshat"))
print(my_sum(1,2,3,4,6.7,9.8))