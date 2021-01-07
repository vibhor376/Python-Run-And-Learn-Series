class Laptop:
    discount=10
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.full_name=brand_name+' '+model_name # we can create an extra or less instance variables 
    def apply_discount(self):
        return self.price-(self.price * Laptop.discount)/100


l1=Laptop("HP","Pavilion",50000)
l2=Laptop("Dell","Inspiron",45000)

print("Before updating discount")
print(f"{l1.full_name}-->{l1.apply_discount()}")
print(f"{l2.full_name}-->{l2.apply_discount()}")

Laptop.discount=15
print("After updating discount")
print(f"{l1.full_name}-->{l1.apply_discount()}")
print(f"{l2.full_name}-->{l2.apply_discount()}")

# Printing the contents of object
print(l1.__dict__) # it will print all the information of object 'l1' in dictionary format
