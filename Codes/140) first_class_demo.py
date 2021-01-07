# Objectives:
# What is a class?
# How to create a class?
# What is init method?
# What are attributes, instance variables?
# How to create an object?

# A class is a blueprint of how it's object will be and what kind of functionality it can perform
# We can compare init method of python with the constructors from the other languages
# Any function defined within the class are known as methods

# creating a class
class Person:  # according to convention it is recommended to use first letter capital in the name of class(it's not mandatory)
    def __init__(self,first_name,last_name,age): # we can write anything in place of 'self' but according to convention we write 'self'
        # Instance variable
        print('__init__ method called!!')
        self.first_name=first_name # we can also write self.person_first_name(or any other name)=first_name 
        self.last_name=last_name  # we can also write self.person_last_name(or any other name)=last_name 
        self.age=age # we can also write self.person_age(or any other name)=age 

# creating objects of the class
p1=Person('Akshat','Bhatnagar',20)  # when __init__ is called 'p1' will be the 'self'
p2=Person("Lekhansh","Bhatnagar",16) # when __init__ is called 'p2' will be the 'self'

print(p1.first_name)
print(p2.age)

# Note: whenever object of class is created __init__ method is called!!

class Person2:
    def __init__(self,first_name,last_name,age):
        print('__init__ method called!!')
        self.fn=first_name
        self.ln=last_name
        self.ag=age

p3=Person2('Akshat',"Bhatnagar",20)
print(p3.fn)
print(p3.ln)
print(p3.ag)