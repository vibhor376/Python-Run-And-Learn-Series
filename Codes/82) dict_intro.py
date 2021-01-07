# Dictionaries are the unordered collection of data in key : value pair

# Creating dictionaries
# Method 1
user={'Name': 'Akshat', 'Age': 20} # syntax for dictionaries
print(user)
print(type(user))

# Method 2
user1=dict(Name='Lekhansh',Age=16)
print(user1)
print(type(user1))

# Accessing items of dictionaries (we use keys to access dictionaries)
print(user['Name'])
print(user['Age'])
print(user1['Name'])
print(user1['Age'])

user_info1={
    'Name':'Akshat',
    'Age' : 20,
    'Hobbies': ['Cricket','Programming','Computer_Games'],
    'Songs': ['Song1','Song2']
}
print(user_info1)
user_info2={
    'Name':'Lekhansh',
    'Age' : 16,
    'Hobbies': ['Cricket','Computer_Games'],
    'Songs': ['Song3','Song4']
}
users={"User1":user_info1,"User2":user_info2}
print(users)

# Adding data to empty dictionary
res={}
res['Name']='Akshat'
res['Age']=20
print(res)