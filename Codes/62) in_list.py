fruits=["apples","mango","grapes","orange","banana"]
text=input("Enter any fruit name: ")
if text in fruits:
    print(f"{text} is present in the list")
else:
    print(f"Sorry! {text} is not present in the list")
