# strings vs lists

# strings are immutable whereas lists are mutable
s="akshat"
s.title()
print(s) # OUTPUT: "akshat" not "Akshat"
t=s.title()
print(t) # OUTPUT: "Akshat" 

l=['Akshat','Lekhansh','Preet']
l.pop()
print(l) # OUTPUT: ['Akshat', 'Lekhansh']
l.append('Vibhor')
print(l) # OUTPUT: ['Akshat', 'Lekhansh', 'Vibhor']