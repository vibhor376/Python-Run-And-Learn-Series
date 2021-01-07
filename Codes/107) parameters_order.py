# Parameters order which declaring a function
# 1) normal parameters
# 2) *args
# 3) default parameters
# 4) **kwargs
def func(name,*args,last_name="unknown",**kwargs):  # this order should be maintained always!!
    print(f"name is {name}")
    print(f"args is {args}")
    print(f"last name is {last_name}")
    print(f"kwargs is {kwargs}")

func("akshat",*[1,2,3],**{"Name":"AKSHAT","Age":20})
func("Lekhansh",1,2,3,Name="LEKHANSH",Age=16)
