# Function returning function

def outer_func():
    def inner_func():
        print("Inside inner function")
    return inner_func
v=outer_func()   # v will point to inner_func
v()

def outer_func2(msg):
    def inner_func2():
        print(f"Message is {msg}")
    return inner_func2
v1=outer_func2("Hello Everyone!!") # v1 will point to inner_func
v1()

