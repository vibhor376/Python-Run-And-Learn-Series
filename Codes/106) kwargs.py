# kwargs (keyword arguments)
# **kwargs (double star operator)
def func(names,**kwargs):
    print(f"name is {names} and kwargs is {kwargs}")
    print(f"Type of kwargs is {type(kwargs)}")
    for k,v in kwargs.items():
        print(f"{k} : {v} ")

func('Lekhansh',first_name="Akshat",last_name="Bhatnagar")  # it will create dictionary
print()
# Dictionary Unpacking
d={'name':'Akshat Bhatnagar','age':'20'}
func('Lekhansh',**d)
