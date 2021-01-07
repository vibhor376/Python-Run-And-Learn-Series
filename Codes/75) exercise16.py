# Write a function which takes 2 lists as an argument and returns the common elements in both the lists
def common_list(l1,l2):
    com=[]
    for i in l1:
        if i in l2:
            com.append(i)
    return com

n1=int(input("Enter the number of elements in the 1st list: "))
li1=[]
print("Enter the elements: ")
for i in range(n1):
    li1.append(int(input()))
n2=int(input("Enter the number of elements in the 2nd list: "))
li2=[]
print("Enter the elements: ")
for i in range(n2):
    li2.append(int(input()))

new_list=common_list(li1,li2)
print(new_list)