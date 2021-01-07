# Instance methods
l=[1,2,3,4]
l.pop() # this is an instance method for list class

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return self.first_name+' '+self.last_name
    def is_above_18(self):
        return self.age>18

# Note: Always remember to give object as a first argument while defining a method(or function) of class

p1=Person('Akshat','Bhatnagar',20)
p2=Person("Lekhansh","Bhatnagar",16)

print(p1.full_name())
print(Person.full_name(p1))  
# These two lines will give same output!

print(p2.full_name())
print(Person.full_name(p2))
# These two lines will give same output!

print(p1.is_above_18())
print(p2.is_above_18())

l1=[1,2,3]
l2=[1,2,3]
l1.clear()
print(l1)
list.clear(l2)
print(l2)

l1.append(10)
print(l1)
list.append(l2,10)
print(l2)