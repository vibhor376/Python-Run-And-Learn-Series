# Our task is to extract all the links from the given html file 'htmlfile.html' and write them into a text file
# Note: find function of string returns -1 searched element is not in the string

# Method 1) --> this method cannot extract multiple links in single line
with open('htmlfile.html','r') as rf:
    with open('links.txt','w') as wf:
        for i in rf.readlines():
            if '<a href=' in i:
                pos=i.find('<a href=')
                first_quote=i.find("\"",pos)
                second_quote=i.find("\"",first_quote+1)
                url=i[first_quote+1:second_quote]
                wf.write(url+"\n")

# Method 2) --> it will deal with previous mentioned problem!
with open('htmlfile.html','r') as rf1:
    with open('links2.txt','w') as wf1:
        page=rf1.read()
        link_exist=True
        while link_exist:
            pos=page.find('<a href=')
            if pos==-1:
                link_exist=False
            else:
                first_quote=page.find("\"",pos)
                second_quote=page.find("\"",first_quote+1)
                url=page[first_quote+1:second_quote]
                wf1.write(url+"\n")
                page=page[second_quote:] 
        