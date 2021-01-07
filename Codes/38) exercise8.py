# our target is to print count of every character including spaces in a give string entered by the user
text=input("Enter any text: ")
print("Count of Characters are as follows: ")
i=0
pat=""
while i<len(text):
    if (not pat)or (not text[i] in pat):
        print(f"{text[i]} : {text.count(text[i])}")
        pat+=text[i]
    i+=1
