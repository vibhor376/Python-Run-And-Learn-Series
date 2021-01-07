# Create a laptop class with attributes like brand name, model name, price
# Create two instance(object) of your laptop class
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.full_name=brand_name+' '+model_name # we can create an extra or less instance variables 

l1=Laptop("HP","Pavilion",50000)
l2=Laptop("Dell","Inspiron",45000)

print(f"Brand Name: {l1.brand_name}, Model Name: {l1.model_name}, Price: {l1.price}, Full Name: {l1.full_name}")
print(f"Brand Name: {l2.brand_name}, Model Name: {l2.model_name}, Price: {l2.price}, Full Name: {l2.full_name}")