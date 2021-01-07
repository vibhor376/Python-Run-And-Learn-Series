name,char=input("ENTER A NAME AND A CHARACTER ").split(",")
print(len(name.strip()))
print(f"{name.lower().strip().count(char.lower().strip())}")