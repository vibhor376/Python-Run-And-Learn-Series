# Our task is to read the content from one file and write it to another blank file
with open('sample2.txt','r') as rf:
    with open('sample2(copy).txt','w') as wf:
        wf.write(rf.read())
        
