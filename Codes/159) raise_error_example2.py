class Mobile:
    def __init__(self,name):
        self.name=name

class MobileStore:
    def __init__(self):
        self.mobiles=[]

    def add_mobiles(self,mobile):
        if(isinstance(mobile,Mobile)):
            self.mobiles.append(mobile)
        else:
            raise TypeError("Mobile you want to add must be an object of Mobile class!")

m1=Mobile('OnePlus 7')
m2='Samsung Note 9'
ms=MobileStore()
ms.add_mobiles(m1)
print(ms.mobiles) # object will get printed!!
print([i.name for i in ms.mobiles]) # this will print the contents of the object!
ms.add_mobiles(m2) # this will give a TypeError, since m2 is not an instance (or object) of class Mobile
