# Given a file named salary.txt which contains
# Name,salary
# Example : salary.txt
# Akshat,500
# Lekhansh,250
# Preet, 400

# your target is to create a new file which contains entries like
# Akshat's Salary is 500
# Lekhansh's Salary is 250
# Preet's Salary is 400

with open('salary.txt','r') as rf:
    with open('new_format.txt','w') as wf:
        for i in rf.readlines():
            name,salary=i.split(",")
            wf.write(name+"\'s Salary is "+salary)

        
