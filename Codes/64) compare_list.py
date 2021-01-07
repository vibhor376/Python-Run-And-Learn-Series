# compare lists

fruits1=['apple','banana','orange','grapes']
fruits2=['apple','banana','orange','grapes']
fruits3=['apple','kiwi','guava']

print(fruits1==fruits2)  # OUTPUT: True since both of them are same list with different name
print(fruits1==fruits3)  # OUTPUT: False since both of them are different
print(fruits1 is fruits2) # OUTPUT: False, 'is' checks whether these two list are allocated to same memory or not
print(fruits1 is fruits1) # OUTPUT: True
