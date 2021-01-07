# Dictionary Comprehension with if else statements

# we have to create a dictionary in such a way that when key is odd then it's value will be 'odd' and same goes with even keys
# Method 1)--> without dictionary comprehension
d={}
for i in range(1,11):
    if i%2:
        d[i]='odd'
    else:
        d[i]='even'
print(d)
# Method 2)--> with dictionary comprehension
d1={i:('odd' if i%2 else 'even') for i in range(1,11)}
print(d1)