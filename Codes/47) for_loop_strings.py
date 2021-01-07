name=input("Enter any text: ")
# using standard method
print("By Standard Method") 
for i in range(len(name)):
    print(name[i],end="")  # end="" means every output will print next to each other not on the new line by default it is newline
print()
# using python power!!
print("Using Python Power!!")
for i in name:
    print(i,end="")