# Special magic methods / dunder methods
# operator overloading
# polymorphism

class Phone:  
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)  # this is to deal with -ve prices entered by the user
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def __str__(self): 
        return f"{self.brand} {self.model_name} {self._price}"
   
    def __repr__(self):
        return f"Phone(\'{self.brand}\',\'{self.model_name}\',{self._price})"
    
    def __len__(self):
        return len(self.full_name())
    
    def __add__(self,other):  # this is called operator overloading
        return self._price + other._price

# __name__ --> these are known as dunder methods
p1=Phone('Nokia','1100',1000)
print(p1) # By the use of __repr__  or __str__ it will print brand, model_name, _price. Otherwise it will print the object location in memory
print(repr(p1))
print(str(p1))
print(len(p1))
# 2 + 5 =7 and 'abc'+'def'='abcdef' this is an example of operator overloading
p2=Phone('Mi','7s',13000)
print(p1+p2) # this will call __add__ function and will return the sum of prices of both phones!!

# Polymorphism --> it means having many forms. Example :- 2+3=5 and 'ab'+'cd'='abcd' here '+' operator has 2 different form so,
# operator overloading is an example of polymorphism. Also method overriding is an example of polymorphism

class SmartPhone(Phone):
    def __init__(self, brand, model_name, price,camera):
        super().__init__(brand, model_name, price)
        self.camera=camera

    def full_name(self):  # Method overriding
        return f"{self.brand} {self.model_name} {self.camera}"
p3=SmartPhone('OnePlus','6T',34000,'32 MP')
print(p3.full_name())
print(p1.full_name())