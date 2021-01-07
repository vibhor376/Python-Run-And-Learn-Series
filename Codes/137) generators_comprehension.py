# Genrators comprehension

square=[i**2 for i in range(1,11)]  # list comprehension
print(square)

square1=(i**2 for i in range(1,11)) # generator comprehension
print(square1)

for i in square1:
    print(i)

for i in square1:
    print(i)
# Notice that it will print only once!!

square2=(i**2 for i in range(1,5)) # generator comprehension
print(next(square2))
print(next(square2))
print(next(square2))
print(next(square2))