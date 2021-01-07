# What are docstrings?
# How to write doctrings?
# How to see docstrings?
# What is help function?

def tot(a,b):
    '''This function takes 2 arguments and returns their sum '''  # this is called docstrings
    return a+b
print(tot(4,5))

print(tot.__doc__) # this will print the docstring of the function 'tot'
print(len.__doc__) # this will print the docstring of the function 'len' 
print(sum.__doc__) # this will print the docstring of the function 'sum'

# Help function
print(help(sorted))
print(help(max))