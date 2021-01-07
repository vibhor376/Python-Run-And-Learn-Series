# Write a function which takes a list as an argument and reverse it 
# Use only append() and pop() !!
def rev_list(l):
    rev=[]
    while l:
        rev.append(l.pop())
    return rev

n=int(input("Enter the number of elements in the list: "))
li=[]
print("Enter the elements: ")
for i in range(n):
    li.append(int(input()))

new_list=rev_list(li)
print(new_list)