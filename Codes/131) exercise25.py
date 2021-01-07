from functools import wraps
import time
# Write a function which calculates square of all numbers from 1 to n and use a decorator funtion to print it's execution time

def calc_time(any_function):
    @ wraps(any_function)
    def wrapper(*args,**kwargs):
        print(f"Executing.... {any_function.__name__}")
        t1=time.time()   # starting the timer
        r=any_function(*args,**kwargs)
        t2=time.time()   #  ending the timer
        print(f"This function took {t2-t1} seconds")
        return r
    return wrapper

@ calc_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

print(square_finder(5))
print(square_finder(14))
square_finder(100000)