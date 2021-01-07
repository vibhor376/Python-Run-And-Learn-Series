# Python custom exception
# we use this to increase readability of the code

class NameIsTooShortError(ValueError):  # by this we inherit our new class from ValueError so we can use it inplace of ValueError!!
    pass

def validate(s):
    if len(s)<8:
        raise NameIsTooShortError("Too short username!")

username=input("Enter you username: ")
validate(username)
print(f"Hello {username} !")