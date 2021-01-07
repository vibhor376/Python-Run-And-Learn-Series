# Write a function which takes list as an argument and return a list which contains square of the elements of the passed list
def sq_list(l):
    sq=[]
    for i in l:
        sq.append(i*i)
    return sq
n=int(input("Enter the number of elements in the list: "))
li=[]
print("Enter the elements: ")
for i in range(n):
    li.append(int(input()))

new_list=sq_list(li)
print(new_list)