# in keyword in sets and loops
s={'a','b','c'}

# in keyword
ch=input('Enter an element to be checked: ')
if ch in s:
    print('Present')
else:
    print('Not Present')

# loops
# for loop
for i in s:
    print(i)

# set math 
s1={1,2,3,4}
s2={3,4,5,6}

# 1) Union --> it combines all the values from the both sets
print(s1.union(s2))  
print(s1|s2)  

# 2) Difference 
print(s1.difference(s2))  # it will remove the common values between s1 and s2 from s1
print(s1-s2)
print(s2-s1) # it will remove the common values between s1 and s2 from s2

# 3) Intersection --> it gives the common values between two sets
print(s1.intersection(s2))
print(s1&s2)