mixed=(1,2,3,4.0)

# looping in tuple
# 1) for loop
for i in mixed:
    print(i)
# 2) while loop
i=0
while i<len(mixed):
    print(mixed[i])
    i+=1

# tuple with one element
num=(1) # most of us will declare this way at first but it's wrong if you check type of num it will be an integer not tuple
print(type(num))
num1=(1,) # this way you can declare a tuple with single element!!
print(type(num1))

# tuple without paranthesis
cars='Mahindra','TATA','Maruti'  # it will create a tuple!!
print(type(cars))
print(cars)

# tuple unpacking
car1,car2,car3=(cars)  # Make sure that no. of variables should be equal to no. of elements in the tuple
print(car1)
print(car2)
print(car3)

# list inside tuple
hobbies=('Cricket',['Competitive Programming','Computer games'])
print(hobbies)
hobbies[1].pop()
print(hobbies)
hobbies[1].append('T.V.')
print(hobbies)

# min,max,sum functions
print(max(mixed))
print(min(mixed))
print(sum(mixed))