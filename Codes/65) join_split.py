# 1) split method -- it will convert string into list
user_info="Akshat 20".split()  # split() will split the input where " " occurred and user_info will be converted into list 
print(type(user_info)) # type will tell the data type of the passed variable
print(user_info)
name,age=input("Enter your name and age: ").split(",")
print(f"Your Name is: {name} and your age is: {age}")

# 2) join method -- it will convert list into string
user=['Akshat','20']
print(','.join(user))  # OUTPUT: Akshat,20
print(' '.join(user))  # OUTPUT: Akshat 20