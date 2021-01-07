# Class Variables
class Circle:
    pi=3.14 # Class variable
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*Circle.pi*self.radius  # since pi is class object we access it as "Circle(class_name).pi"
    def area(self):
        return Circle.pi*self.radius*self.radius

c1=Circle(7)
c2=Circle(2)
cir1=c1.circumference()
cir2=c2.circumference()
a1=c1.area()
a2=c2.area()
print(f"Circle with radius {c1.radius} has Area: {a1} and Circumference: {cir1}")
print(f"Circle with radius {c2.radius} has Area: {a2} and Circumference: {cir2}")