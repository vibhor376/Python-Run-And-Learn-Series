# Write a function which takes list as an argument and reverse every element of the list
def rev_each(l):
    rev=[]
    for i in l:
        rev.append(i[::-1])
    return rev

n=int(input("Enter the number of elements in the list: "))
li=[]
print("Enter the elements: ")
for i in range(n):
    li.append(input())

new_list=rev_each(li)
print(new_list)