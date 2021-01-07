with open(r'C:\Users\HP\Desktop\New Year Write Up!.txt','r',encoding='utf-8') as f:
    print(f.encoding) # it will print the encoding of the file
    data=f.read(25)  # it will read upto 25 character at once
    while len(data)>0:
        print(data)
        data=f.read(25)
    