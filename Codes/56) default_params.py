# default parameters
def user_info(first_name,last_name,age=10):
    print(f"Your First Name is {first_name}")
    print(f"Your Last Name is {last_name}")
    print(f"Your age is {age}")
user_info("Akshat","Bhatnagar",20)
user_info("Akshat","Bhatnagar") # if you forgot to mention third argument then the default argument will print
user_info("Lekhansh","Bhatnagar",16)  # if you pass the third argument then function will overwrite the default agrument and print the passed argument

def user_info1(first_name,last_name="Unknown",age=20):
    print(f"Your First Name is {first_name}")
    print(f"Your Last Name is {last_name}")
    print(f"Your age is {age}")
# user_info1("Akshat",19) this will give you an error because you can't pass any argument after default argument