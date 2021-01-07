# Zip function

user_id=['user1','user2','user3']
names=['Akshat','Lekhansh','Preet']
last_name=['Bhatnagar','Bhatnagar','Kothari']
z_o=zip(user_id,names) # z_o is an zip object iterator
print(z_o)
print(list(z_o)) # it will be list of tuples

user_id1=['user1','user2']
z_o1=zip(user_id1,names)
print(z_o1)
print(tuple(z_o1)) # it will be tuple of tuples
# Notice that length of user_id1 < names so it will zip the items from names and user_id1 untill all the elements of user_id1 are used 
# up and left element of the list will not be present in the z_o1

example=[('a',1),('b',2),('c',3)]
d=dict(example)  # we can always convert this type of lists into dictionaries!!
print(d)

user_id2=['User1','User2','User3']
print(dict(zip(user_id2,names)))

user_id3=["USER1","USER2","USER3"]
print(list(zip(user_id3,names,last_name)))  # same you cannot do to form dictionary!!