# fibonacci series
# 0 1 1 2 3 5 8 13 21......
# every term of the series is sum of the previous two terms!
def fibonacci(num):
    f,s,i=0,1,2
    if num==1:
        print("0")
    else:
        print(f,s,end=" ")
        while i<num:
            c=f+s
            print(c,end=" ")
            f=s
            s=c
            i+=1
n=int(input("Enter the number of terms you want to print of Fibonacci series: "))
fibonacci(n)