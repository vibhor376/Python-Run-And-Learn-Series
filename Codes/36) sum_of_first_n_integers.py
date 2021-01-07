n=int(input("Enter a Number: "))

# Method One (Using while loop)
i=1
s1=0
while i<=n:
    s1+=i
    i+=1
print(f"Sum using while loop is: {s1}")

# Method Two (Using Mathematical Formula)
print(f"Sum using Mathematical Formula is: {((n+1)*n)//2}")