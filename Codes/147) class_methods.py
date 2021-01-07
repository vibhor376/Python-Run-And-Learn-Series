# Class methods

class Person:
    c=0
    
    def __init__(self,first_name,last_name,age):
        Person.c+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    @ classmethod    # this is how we create class methods
    def count_instances(cls):
        return f"You have created {cls.c} instances of {cls.__name__} class"
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def is_above_18(self):
        return self.age>18

p1=Person('Akshat','Bhatnagar',20)
print(Person.count_instances())
p2=Person("Lekhansh","Bhatnagar",16)
print(Person.count_instances())

# We can do the followings, but one should avoid this in general!
print(p1.count_instances())
print(p2.count_instances())