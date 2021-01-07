# Lists vs Generators
import time
t1=time.time()
l=[i**2 for i in range(10000000)] # it will take much memory and will take some time to execute
t2=time.time()

t3=time.time()
g=(i**2 for i in range(10000000)) # it will take very less memory an will quickly execute
t4=time.time()

print(f"Time by list {t2-t1} seconds")
print(f"Time by generator {t4-t3} seconds")