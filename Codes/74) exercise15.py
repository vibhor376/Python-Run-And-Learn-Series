# Write a function which takes list as an argument and filter it to two lists(one contains odd number and one contains even number)
# example-->  [1,2,3,4]  then output should be [[1,3], [2,4]]
def odd_even(l):
    o=[]
    e=[]
    for i in l:
        if i%2:
            o.append(i)
        else:
            e.append(i)
    return [o,e]

n=int(input("Enter the number of elements in the list: "))
li=[]
print("Enter the elements: ")
for i in range(n):
    li.append(int(input()))

new_list=odd_even(li)
print(new_list)