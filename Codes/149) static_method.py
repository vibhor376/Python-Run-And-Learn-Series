class Person:
    c=0
    
    def __init__(self,first_name,last_name,age):
        Person.c+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    @ classmethod
    def from_string(cls,string):
        first,last,age=string.split(",")
        return cls(first,last,int(age))
    
    @ classmethod    # this is how we create class methods
    def count_instances(cls):
        return f"You have created {cls.c} instances of {cls.__name__} class"
    
    @ staticmethod
    def hello():
        print("Hello, static method was called!!")

    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def is_above_18(self):
        return self.age>18
p1=Person('Akshat','Bhatnagar',20)
p2=Person("Lekhansh","Bhatnagar",16)
Person.hello()
