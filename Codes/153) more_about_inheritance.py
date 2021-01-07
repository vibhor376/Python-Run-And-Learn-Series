# Can we derive more than one class for base class?
# Multilevel inheritance
# Method resolution order
# Method overriding
# isinstance(), issubclass()

class Phone:  # Base class/parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)  # this is to deal with -ve prices entered by the user

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}....")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

class SmartPhone(Phone): # derived/child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price) 
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    
    def full_name(self):   # This is called method overriding 
        return f"{self.brand} {self.model_name} and Price is {self._price}"

class SmartPhone2(Phone): # derived/child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,os):
        super().__init__(brand,model_name,price) 
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
        self.os=os

p1=Phone('Nokia','3312',1340)
p2=SmartPhone('OnePlus','6T',45000,'6 GB','64 GB','48 MP')
p3=SmartPhone2('Iphone','11x',100000,'8 GB','128 GB','48 MP','IOS')
print(p1.full_name())
print(p2.full_name()) # this will execute the "full_name" method of "SmartPhone" class not the inherited "full_name" method and this what we call as method overriding!!
print(p3.full_name())

class FlagshipPhone(SmartPhone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera
    
    

# Note: Classes "Smartphone" and "SmartPhone1" are derived from "Phone" class so this is called hierarchical inheritance
# Note: Class "FlagshipPhone" is derived from "Smartphone" which inturn is derived from class "Phone" so this it called multilevel inheritance

p4=FlagshipPhone('Samsung','Note 9',50000,'6 GB','128 GB','48 MP','30 MP')
print(p4.full_name()) # This will execute the "full_name" which was override in the class "SmartPhone"

# Method resolution order is the order in which python searches for methods or instances in a class
print(help(FlagshipPhone))

# isinstance --> it checks whether an instance belongs to a specific class or not
print(isinstance(p4,FlagshipPhone)) # Output: True
print(isinstance(p4,SmartPhone))  # Output: True, due to inheritance!!
print(isinstance(p2,FlagshipPhone))  # Output: False
print(isinstance(p2,Phone)) # Output: True, due to inheritance!!

# issubclass --> it checks whether a class is a subclass of another class or not
print(issubclass(FlagshipPhone,SmartPhone))  # Output: True 
print(issubclass(SmartPhone,Phone))  # Output: True
print(issubclass(SmartPhone2,SmartPhone))  # Output: False
print(issubclass(Phone,Phone)) # Output: True, a class is subclass of itself!!
