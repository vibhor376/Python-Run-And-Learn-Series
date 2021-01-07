# with block is used to read or write a file and this automatically closes the file when work on it is done!!
with open('sample.txt') as f:
    print(f.read())
print(f.closed) # Output will be false as it will automatically close the file!!