# Dictionary Comprehension

# We want to create the dictionary --> square={1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}
# Method 1)--> without dictionary comprehension
d={}
for i in range(1,11):
    d[i]=i**2
print(d)  
# Method 2)--> with dictionary comprehension  
d1={num:num**2 for num in range(1,11)}
print(d1)
d2={f"Square of {num} is":num**2 for num in range(1,11)}
print(d2)
for k,v in d2.items():
    print(f"{k} : {v}")

# We want to get counts of all the characters in the string
# Method 1)--> without dictionary comprehension
d3={}
name="akshat bhatnagar"
for i in name:
    d3[i]=name.count(i)
print(d3)
# Method 2)--> with dictionary comprehension
d4={i:name.count(i) for i in name}
print(d4) 