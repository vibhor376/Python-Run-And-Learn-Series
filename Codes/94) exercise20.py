# Write a program which takes list of strings from the user and reverses each element of the list (Use list comprehension)
l=list(input("Enter list elements comma separated ").split(","))
print([i[::-1] for i in l])