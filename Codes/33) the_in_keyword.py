name="Akshat"
ch=input("Enter a Character to be searched ")
if ch in name:  # it is Case sensitive !!
    print(f"{ch} is present in {name}")
else:
    print(f"{ch} is not present in {name}")