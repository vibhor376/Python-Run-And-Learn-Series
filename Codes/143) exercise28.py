# Create a laptop class with attributes like brand name, model name, price and create a function 'apply_discount' which takes a number(n)
# as an argument and discounts the price by n%
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.full_name=brand_name+' '+model_name # we can create an extra or less instance variables 
    def apply_discount(self,d):
        return self.price-(self.price * d)/100

l1=Laptop("HP","Pavilion",50000)
l2=Laptop("Dell","Inspiron",45000)

print(f"Price of laptop {l1.full_name} before discount is: {l1.price}")
print(f"Price of laptop {l2.full_name} before discount is: {l2.price}")

p1=l1.apply_discount(12)
p2=l2.apply_discount(5)

print(f"Price of laptop {l1.full_name} after some discount is: {p1}")
print(f"Price of laptop {l2.full_name} after some discount is: {p2}")