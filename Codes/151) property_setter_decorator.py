class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)  # this is to deal with -ve prices entered by the user
        self.complete_specifications= f"{self.brand} {self.model_name} and price is {self._price}"

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}....")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

p1=Phone('Nokia','3300',1200)
print(p1.brand)
print(p1.model_name)
p1._price=500  
print(p1._price)
print(p1.complete_specifications) # But we can see that even after changing the price it's not refected here

# so to fix this let's define the class as follows

class Phone1:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)  # this is to deal with -ve prices entered by the user
    
    @ property  # so by this we can call it like an instance instead of like a function
    def complete_specification(self):  # instead of using an instance of 'complete_specifications' in __init__, define a separate function 
        return f"{self.brand} {self.model_name} and price is {self._price}"

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}....")
    
    @ property
    def price(self):
        return self._price
    
    @price.setter  # this is used to deal with problems when user updates a value of price with a -ve number
    def price(self,new_price):
        self._price = max(0,new_price)
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

p2=Phone1('Nokia','3300',1200)
p2.price=500  
print(p2.price) # this will also print the price
print(p2.complete_specification) # now change of price will be refected here also!!
p2.price=-100
print(p2.complete_specification) # the price will be 0