# Multiple Inheritance
class A:
    def Class_A_Method(self):
        return "I\'m Just a Class A method!!"
    def hello(self):
        return 'Hello from class A'
    
a=A()
print(a.Class_A_Method())
print(a.hello())

class B:
    def Class_B_Method(self):
        return "I\'m Just a Class B method!!"
    def hello(self):
        return 'Hello from class B'

class C(A,B):  # this is called multiple inheritance
    pass

c=C()
print(c.Class_A_Method())
print(c.Class_B_Method())
print(c.hello()) # "hello" method of class A will be executed since we are writing C(A,B) if we have written C(B,A) then "hello" method of class B would have been executed
print(C.mro()) # this will give the method resolution order of Class in list format
print(C.__mro__) # this will also give the method resolution order of Class in tuple format