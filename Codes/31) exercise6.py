name,age=input("Enter Your Name And Age (space separated): ").split()
if (name[0]=="a" or name[0]=="A") and int(age)>=10:
    print("You Can Watch The 'COCO' Movie !")
else:
    print("Sorry, You Cannot Watch The 'COCO' Movie !")