user_info={
    'Name':'Akshat',
    'Age' : 20,
    'Hobbies': ['Cricket','Programming','Computer_Games'],
    'Songs': ['Song1','Song2']
}

# check if key exists in dictionary
if 'Name' in user_info:
    print("Present")
else:
    print("Not_Present")

# check if value exists in dictionary
if 'Akshat' in user_info:  # this will check the key not the value
    print("Present")
else:
    print("Not_Present")
if 'Akshat' in user_info.values(): # this will check for values
    print("Present")
else:
    print("Not_Present")

# loops in dictionaries
for i in user_info:  # all keys will get printed
    print(i)   
for i in user_info.values(): # all values will get printed
    print(i)
for i in user_info:  # another way of printing the values
    print(user_info[i])

# values method
user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

# keys method
user_info_keys=user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# items method
user_item=user_info.items()
print(user_item)
print(type(user_item))

for key,value in user_info.items():
    print(f"Key is {key} and corresponding value is {value}")
for i in user_info.items():
    print(i)