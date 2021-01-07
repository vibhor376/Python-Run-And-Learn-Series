fruits=['grapes','mango','apple']
fruits.sort()
print(fruits)

fruits1=('grapes','mango','apple')
# fruits1.sort() --> it is not possible to sort the tuples !
print(sorted(fruits1)) # it will print the list in sorted order
print(fruits1)  # but original tuple will remain same

fruits2={'grapes','mango','apple'}
# fruits2.sort() --> it is not possible to sort the sets also !
print(sorted(fruits2)) # it will print the list in sorted order
print(fruits2) # but original set will remain same

cars=[
    {'model':'TATA','price':500000},
    {'model':'Maruti','price':100000},
    {'model':'Audi','price':1000000},
    {'model':'Range rover','price':900000}
]
print(sorted(cars,key=lambda d: d['price'])) # this will print the items of dictionary in sorted order according to 'price'!!
print(sorted(cars,key=lambda d: d['price'],reverse=True)) # this will print the items of dictionary in reverse sorted order according
# to 'price'!!
