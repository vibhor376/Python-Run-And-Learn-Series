user_info={
    'Name':'Akshat',
    'Age' : 20,
    'Hobbies': ['Cricket','Programming','Computer_Games'],
    'Songs': ['Song1','Song2']
}
more_info={'Name':'Akshat Bhatnagar','State':'Rajasthan', 'Languages':['English','Hindi','French']}
user_info.update(more_info) # it will add the key-value pair from "more_info" to "user_info" and will update the key if already present
# in the dictionary
print(user_info)
user_info.update({}) # it will not update anything and dictionary will remain as it is
print(user_info)
