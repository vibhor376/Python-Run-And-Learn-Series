# Set Comprehension
s=set(range(1,11))

# we want to create a set --> {1,4,9,16,25,36,49,64,81,100}
# Method 1)--> without set comprehension
sq=set()
for i in range(1,11):
    sq.add(i**2)
print(sq)
# Method 2)--> with set comprehension
sq1={i**2 for i in range(1,11)}
print(sq1)

# we want to create a set which contain first letter of the given list of strings
l=['Akshat','Lekhansh','Vibhor','Yatharth']
s={i[0] for i in l}
print(s)

