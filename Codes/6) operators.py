#addition 
print(2+3)
#substraction
print(5-6)
#mutiplication
print(9*8)
#floating point division
print(4/5)
print(4/2)
#integer division
print(4//2)
#modulus operator
print(5%3)
#exponential
print(2**3)
print(2**0.5)
#rounding off
print(round(2**0.5,4))
#understanding precedence rules
print(2**3/2*6-4*(3-4/2))
#       operators             precedence and associativity
# 1.  Paranthesis "()"                  Highest
# 2.   Exponent "**"                 Right to Left
# 3.    *,/,//,%                     Left to Right
# 4.       +,-                       Left to Right
print((2+3)*5/2%6)
# step 1: 5*5/2%6
# step 2: 25/2%6
# step 3: 12.5%6
# step 4: 0.5
print(2**3**2)
# step 1: 2**9
# step 2: 512