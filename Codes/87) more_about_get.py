d={'Name':'Akshat','Age':20,'Age':16}  # Since we have declared 'Age' key 2 times then the 'Age':16 will overwrite 'Age':20!!
print(d)
print(d.get('Name'))
print(d.get('Names','Not Found!')) # by default it will return none but this time it will return 'Not Found!'
