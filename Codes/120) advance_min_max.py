# Advanced min() and max()

numbers=[1,2,3,4,5,6]
print(max(numbers))
print(min(numbers))

def func(item):
    return len(item)
names=['Akshat','Lekhansh','Preet']
print(max(names,key=func))  # this will find the maximum according to the length of the string!!
print(min(names,key=func))  # this will find the minimum according to the length of the string!!
print(max(names,key=lambda l: len(l)))  # this will find the maximum according to the length of the string!!
print(min(names,key=lambda l: len(l)))  # this will find the minimum according to the length of the string!!

student={
    'Akshat':{'score':95,'age':20},
    'Lekhansh':{'score':90,'age':16},
    'Preet':{'score':92,'age':20}
}
print(max(student,key=lambda i: student[i]['score']))  # this will find the maximum according to the 'score' !!
print(min(student,key=lambda i: student[i]['score']))  # this will find the minimum according to the 'score' !!
student2=[
    {'name':'Akshat','score':95,'age':20},
    {'name':'Lekhansh','score':90,'age':16},
    {'name':'Preet','score':92,'age':20}
]
print(max(student2,key=lambda i: i.get('score')))  # this will find the maximum according to the 'score' !!
print(min(student2,key=lambda i: i.get('score')))  # this will find the minimum according to the 'score' !!
print(max(student2,key=lambda i: i.get('score'))['name'])
print(min(student2,key=lambda i: i.get('score'))['age']) 

