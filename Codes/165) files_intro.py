# Read file
# Open file
# read method
# seek method
# tell method
# readline method
# readlines method
# Close file

f = open('sample.txt','r') # here 'r' is used but it can be skipped as by default it will open the file in read mode
print(f"Cursor position -- {f.tell()}") # this will tell the current cursor position
print(f.read()) # it will print the content of the file
print(f.read())
# content of the file will only print once since after reading the file for the first time it's cursor has moved to end where there is
# text so f.read() is called again then it will not print the file content one more time 
print("Before seek method")
print(f"Cursor position -- {f.tell()}") # this will tell the current cursor position and notice it has position at the end of text
f.seek(0) # it will set our cursor postion to 0
print("After seek method")
print(f"Cursor position -- {f.tell()}")
f.close() # it will close the file

f=open('sample.txt')
print(f.readline(),end='') # it will print the one line from your text file
print(f.readline()) # it will print another line from your text file
f.close()

f=open('sample.txt')
lines=f.readlines() # this will create list of all the lines in your text file
print(lines)
print(f"No. of lines in your text file is {len(lines)}")
for i in lines: # this will print all the lines
    print(i,end="")
f.close()

f=open('sample.txt')
print(f.name) # this will print the file name
print(f.closed) # this will tell whether the file is closed or not
f.close()
print(f.closed)

f1=open(r"C:\Users\HP\Desktop\fonts.txt") # this is to open the file when it is present in some other location
for i in f1: # this will print all the lines in your text file
    print(i)
f1.close()