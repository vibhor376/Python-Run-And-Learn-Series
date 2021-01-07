# Define a class and write a program which tells how many times the object of this class was created
class Person:
    c=0
    def __init__(self,first_name,last_name,age):
        Person.c+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
p1=Person('Akshat','Bhatnagar',20)
print(f"Number of objects created: {Person.c}")
p2=Person("Lekhansh","Bhatnagar",16)
print(f"Number of objects created: {Person.c}")
