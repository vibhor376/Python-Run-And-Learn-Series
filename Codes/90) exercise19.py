# Our Task is to add the information entered by the user to our dictionary and user should enter the values which are "," separated
user_info={
    'Name':'Akshat',
    'Age' : 20,
    'Hobbies': ['Cricket','Programming','Computer_Games'],
    'Songs': ['Song1','Song2']
}
n=input("Enter Your Name ")
a=int(input("Enter your age "))
h=list(input("Enter your Hobbies separated by comma ").split(","))
s=list(input("Enter your favourite Songs separated by comma ").split(","))
d={}
d['Name']=n
d['Age']=a
d['Hobbies']=h
d['Songs']=s
user_info.update(d)
for key,value in user_info.items():
    print(f"{key} : {value}")
