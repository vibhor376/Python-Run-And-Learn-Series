# Exception Handling
# try except else finally

while True:
    try:
        age=int(input("Enter your age: ")) # if user gives input as 'seven' of any alphabetic input then it will give a value error
        break
    except ValueError: # this will execute when there is value error
        print("Invalid syntax.. Please enter again!")
    except: # this will execute for every error except value error because it was declared above
        print("Unexpected error!!")

# this above loop will run untill user provides a correct input

if age<18:
    print("You can\'t play this game!!")
else:
    print("You can play this game!!")