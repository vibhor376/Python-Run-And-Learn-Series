# Write on a files using: 'w','a','r+'

# 1) 'w' --> if you try to open any file which does not exist using 'w' then it will automatically creates a new file
# and if you try to open an existing file use 'w' the it will delete all the previous content of the file 

with open('sample2.txt','w') as f: 
    f.write('Hello there!!')

# 2) 'a' --> if you open an existing file using this mode then it will set the cursor to the end of file and from there you can write
# or append any new data (note: this will preserve your previous data on file and will allow you to add more data to that file) and 
# append mode will also create a new file if you try to open a non-existing file

with open('sample2.txt','a') as f:
    f.write('\nAppending new data !')
 
# 3) 'r+' --> By this mode we can do both operation i.e. read and write!! and when we write data using this mode the it 
# will start writing from the beginning overwriting the data of the existing file till all the text is written and if still there is
# some text remaining from previous file then that text will remain as it is!. Whenever you try to open a non-existing file using 
# this mode it will give an error instead of creating that file

with open('sample2.txt','r+') as f:  
    f.seek(len(f.read())) # to move cursor at the end of the existing text
    f.write('\nYou can do it!') 
