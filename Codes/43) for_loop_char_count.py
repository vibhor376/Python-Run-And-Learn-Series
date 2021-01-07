# our target is to print count of every character including spaces in a give string entered by the user
text=input("Enter Any Text Here: ")
print("Count of Characters are as follows: ")
pat=""
for i in range(len(text)):
    if text[i] not in pat:
        print(f"{text[i]} : {text.count(text[i])}")
        pat+=text[i]

