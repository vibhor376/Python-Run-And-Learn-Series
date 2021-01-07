# Built in errors
# Exceptions, how to handle them?
# Raise your own errors, debugging, etc.

# Built in errors

# 1) Syntax error --> whenever there is use of wrong syntax 
# 2) Indentation error --> whenever there is any wrong indentation (or tab-spacing) given 
# 3) Name error --> whenever someone tries to access any variable which is not defined
# 4) Type error --> whenever someone tries to perform an operation on a variable which does not supports this operation, eg: 5 +'abc' 
# 5) Index error --> whenever someone tries to access the index which is not in range, eg: l=[1,2,3], print(l[4]) 
# 6) Value error --> eg: s='abc', print(int(s)) this will give value error as 'abc' cannot be converted to int
# 7) Atrribute error --> eg: l=[1,2,3], l.push('4') this will give attribute error as list does not contain any 'push' attribute
# 8) Key error --> eg: d={'name'= 'Akshat'} , print(d['age']) this will give key error since dictionary has no key named 'age'