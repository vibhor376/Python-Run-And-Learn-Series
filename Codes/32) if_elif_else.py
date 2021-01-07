# show ticketing price
'''
    Age      Price(in Rs)
    1-3         free
    4-10        150
    11-60       250
    >60         200 
'''
age=int(input("Enter Your Age: "))
if 0<age<=3:
    print("Free Of Cost")
elif 3<age<=10:
    print("Ticket Price: 150")
elif 10<age<=60:
    print("Ticket Price: 250")
elif age>60:
    print("Ticket Price: 200")
else:
    print("Please Enter A Valid Age !")