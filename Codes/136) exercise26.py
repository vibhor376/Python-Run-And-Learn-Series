# Write a generator function which takes a number as an argument and generate a sequence of all even numbers between 1 and n 

def even(n):
    for i in range(1,n+1):
        if i%2==0:
            yield(i)

print("generating during the loop...")
for i in even(10):
    print(i)

for i in even(10):  
    print(i) 
# Notice that it will print again 

print("After generating and then iterating...")
eve=even(10)
for i in eve:
    print(i)
for i in eve:
    print(i)
# Notice that it will print only once