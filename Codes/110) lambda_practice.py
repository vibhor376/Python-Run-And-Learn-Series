# write a function to check whether a number is even or odd
# Method 1)
def e_o(n):
    if n%2==0:
        return "EVEN"
    return "ODD"
print(e_o(6))
print(e_o(5))
# Method 2) 
eo=lambda n: "EVEN" if n%2==0 else "ODD"
print(eo(6))
print(eo(5))

# write a function which takes string as an argument and return it's last character
# Method 1)
def la(s):
    return s[-1]
print(la("Akshat"))
# Method 2)
las=lambda s: s[-1]
print(las("Akshat"))

# write a function which takes string as an argument and check whether it's length is greater than or equals to 5 or not
# Method 1)
def lec(s):
    if len(s)>=5:
        return "YES"
    return "NO"
print(lec("Akshat"))
print(lec("ABC"))
# Method 2)
lec1= lambda s: "YES" if len(s)>=5 else "NO" 
print(lec1("Akshat"))
print(lec1("ABC"))