name=input("Enter a name: ")
age=int(input("Enter age: "))

print("By 'and' Condition")
if name=="Akshat" and age==20:  # both conditions need to be true to execute if-block
    print("Welcome Master Akshat !")
else:
    print("Welcome Stranger!")

print("By 'or' Condition")
if name=="Akshat" or age==20:  # one of the conditions or both need to be true to execute if-block
    print("Welcome Master Akshat !")
else:
    print("Welcome Stranger!")