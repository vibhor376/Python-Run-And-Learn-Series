# maximum and minimum functions
l=[38,58,28,21,385,59]
print(min(l))  # OUTPUT: 21
print(max(l))  # OUTPUT: 385

def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(l))