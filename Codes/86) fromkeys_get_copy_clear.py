# fromkeys
d=dict.fromkeys(['name','age','height'],'unknown')
# this will create dictionary like this {'name':'unknown','age':'unknown','height':'unknown'}
print(d)
d1=dict.fromkeys(('name','age','height'),'unknown')
print(d1) # same as dictionary d
d2=dict.fromkeys("ABC",'unknown')
# this will create dictionary like this {'A': 'unknown', 'B': 'unknown', 'C': 'unknown'}
print(d2) 
d3=dict.fromkeys(range(1,11),'unknown')
# this will create dictionary like this {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}
print(d3)
d4=dict.fromkeys(['name','age'],['unknown','unknown'])
# this will create dictionary like this {'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown']}
print(d4)

# get method
print(d['name'])
# print(d['names']) this will give you key error
print(d.get('name'))
print(d.get('names')) # it will not give error but instead it will print none
if d.get('name'):
    print("Present")            # Note: if None: will give you False !!
else:
    print("Not present")

# clear method
d.clear()  # it will clear all the key-value pairs from the dictionary
print(d)

# copy method
d5=d1.copy() # all the key-value pairs of d1 will get copied to d5
print(d1)
print(d5)
# if we have used d5=d1 then both d1 and d5 will be pointing to same dictionary but by using copy method we get a separate copy for d5
d6=d1
print(d5 is d1) # OUTPUT: False
print(d6 is d1) # OUTPUT: True