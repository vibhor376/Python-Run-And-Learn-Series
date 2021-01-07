# NotImplementedError
# Abstract method

class Animals:
    def __init__(self,name):
        self.name=name
    
    def sound(self): # this is called abstract method
        raise NotImplementedError("You Have To Define This Method In Subclasses As Well!!") # this is done because sound of dogs and cats cannot be same :) !!

class Dog(Animals):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    
    def sound(self): # now by defining it here it will not give the NotImplementedError !
        print("Bark! Bark!")

class Cat(Animals):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    
    def sound(self): # now by defining it here it will not give the NotImplementedError !
        print("Meow! Meow!")

d=Dog('Boony','Pug')
d.sound()
c=Cat('Tom','persian')
c.sound()