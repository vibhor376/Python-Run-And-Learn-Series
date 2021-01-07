name=input("Enter any text: ")
d={}
for i in name:
    d[i]=name.count(i)
print(f"Your word count is: {d}")
# Note: order of output may differ because dictionary is unordered collection of data