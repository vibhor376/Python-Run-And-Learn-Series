# Else and Finally clause in exception handling
while True:
    try:
        age=int(input("Enter your age: ")) # if user gives input as 'seven' of any alphabetic input then it will give a value error
    except ValueError:
        print("Invalid syntax.. Please enter again!")
    except: 
        print("Unexpected error!!")
    else:  # this will execute when user inputs the number correctly!!
        print(f"User Input = {age}")
        break 
    finally: # this will execute everytime whether the input is valid or invalid!!
        print("Finally Block.....")
