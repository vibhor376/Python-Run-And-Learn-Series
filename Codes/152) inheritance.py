class Phone:  # Base class/parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)  # this is to deal with -ve prices entered by the user

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}....")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

# We want to define a class named "Smart phone" which not only contains all the features of class "Phone" but also some extra features

class SmartPhone(Phone): # derived/child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        # there are two ways by which we can make __init__ of parent class to handle the common instances
        # Phone.__init__(self,brand,model_name,price)   # this is very uncommon way
        super().__init__(brand,model_name,price) # this is mostly used 
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

p1=Phone('Nokia','3312',1340)
p2=SmartPhone('OnePlus','6T',45000,'6 GB','64 GB','48 MP')
print(p1.__dict__)
print(p2.__dict__)
print(p1.full_name())
print(p2.full_name())