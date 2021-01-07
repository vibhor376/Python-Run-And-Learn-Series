n=input("Enter A Number: ")
c=0
for i in range(len(n)):
    c+=int(n[i])
print(f"Sum of Digits of given number is : {c}")