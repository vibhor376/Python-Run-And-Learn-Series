''' Write a function which takes an integer n as an agrument and returns the dictionary with key varying from 1 to n and values as cube
 of the corresponding keys '''
def ret_d(n):
    d={}
    for i in range(1,n+1):
        d[i]=i**3
    return d
n=int(input("Enter the value of n: "))
res=ret_d(n)
print(f"Your desired dictionary is {res}")
