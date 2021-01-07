# Encapsulation
# Abstraction
# Some special naming convention
# Name Mangling

# Encapsulation means wrapping up of all the datas and their functionalities into one entity
# Abstraction means hiding all the complexities from the user behind any function

l=[1,4,2,3]
l.sort() # tim sort --> the user do not know the mechanism behind this sort function and this is called abstraction
print(l)  

# Everything in python is public!!

class Phone:
    def __init__(self,brand,model_name,price,year):
        self.brand=brand
        self.model_name=model_name
        self._price=price   # _price is to indicate user to not to modify it (it's private!!) but actually it is still public 
        self.__year=year # Name mangling
    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}....")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

# __name__ --> dunder/magic methods
# _name --> it is the convention for private name
# _Classname__name --> Name mangling

phone1=Phone('Nokia','2312',1200,2002)
print(phone1._price)
phone1._price=1100
print(phone1._price)
print(phone1.__dict__)
phone1.__year=2001
print(phone1.__year)
