# Write a function which takes list of strings as an argument and returns the list with each element reversed 
# and first letter capitalized

def func(l,**kwargs):
    if kwargs.get("reverse_str")==True:
        print([i[::-1].title() for i in l])
    else:
        print([i.title() for i in l])

func(["akshat","lekhansh"],reverse_str=True)
func(["akshat","lekhansh"])

