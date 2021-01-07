user_info={
    'Name':'Akshat',
    'Age' : 20,
    'Hobbies': ['Cricket','Programming','Computer_Games'],
    'Songs': ['Song1','Song2']
}

# adding data to dictionary
user_info['Languages']=['English','Hindi','French']
print(user_info)

# pop method
popped_item=user_info.pop('Languages')
print(popped_item) # will print the popped items
print(type(popped_item))
print(user_info) 

# popitem method
pop_item=user_info.popitem() 
print(pop_item) # it will randomly print the popped item
print(type(pop_item))
print(user_info)
