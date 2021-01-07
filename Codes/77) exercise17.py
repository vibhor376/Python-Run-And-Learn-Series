# Write a function which takes list as an argument and gives the count of lists present inside this list
def count_list(l):
    c=0
    for i in l:
        if type(i)==list:
            c+=1
    return c

l1=[1,2,3,[4,5,6],[7,8],9,10,11]
print(count_list(l1))