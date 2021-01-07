# 1) break statement
for i in range(1,11):
    if(i==5):  # as soon as i becomes equals to 5 loop will break ! and it will come out of loop
        break
    print(i)
print("\n")
# 2) continue statement
for i in range(1,11):
    if(i==5): # as soon as i becomes equals to 5 the continue statment will skip the 'print(i)' part and will head towards next iteration
        continue
    print(i)