# Write a function which take two numbers as argument and prints their divsion and handle the exception for divide by zero and TypeError

def divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as err:
        print(err) # this will print the default error message
    except TypeError:
        print("Please enter only numbers!!")
    except:
        print("Unexpected error occured!")
        
divide(4,5)
divide(4,0)
divide('4',3)