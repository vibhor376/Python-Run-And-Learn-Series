# our objective is to print sum of digits of a given number entered by the user
c=0
n=input("Enter a Number: ")
i=0
while i<len(n):
    c+=int(n[i])
    i+=1
print(f"Sum of Digits of a given Number is: {c}")
