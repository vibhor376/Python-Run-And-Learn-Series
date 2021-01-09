# A regular exepression is a special text string for describing a search pattern
import re

String='Akshat is 20 and Lekhansh is 16'

# 1) findall() --> to find all the patters of similar types in the given string

names=re.findall(r"[A-Z][a-z]*",String) # for alphabets ( here [A-Z][a-z]* means selecting pattern which has both lower and upper case letters)

age=re.findall(r'\d',String)  # by this it will create a list of of one digit numbers

print(names) # this will print : ['Akshat', 'is', 'and', 'Lekhansh', 'is'] ; that is all the alphabets pattern!

print(age) # this will print : ['2', '0', '1', '6'] ; that is all the digits pattern!

age2=re.findall(r'\d{1,2}',String) # by this it will create a list of of two digit numbers
print(age2) # this will print : ['20', '16']

names2=re.findall(r'[A-Z]',String) # for alphabets ( here [A-Z] means selecting only upper case letters)
print(names2) # this will print : ['A','L']

names3=re.findall(r'[a-z]',String) # for alphabets ( here [a-z] means selecting only lower case letters)
print(names3) # this will print : ['k', 's', 'h', 'a', 't', 'i', 's', 'a', 'n', 'd', 'e', 'k', 'h', 'a', 'n', 's', 'h', 'i', 's']

# Note: if we write names2=re.findall(r'[A-Z]',String) then it would have included the spaces also and same case for names3

names4=re.findall(r'[A-Z]*',String)
print(names4) # this will print : ['A', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'L', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

names5=re.findall(r'[a-z]*',String)
print(names5) # this will print : ['', 'kshat', '', 'is', '', '', '', '', 'and', '', '', 'ekhansh', '', 'is', '', '', '', '']

test="He is very cool. He is awsome!"

matches=re.findall("is",test) # this will find all the "is" from the given text and make a list of them
print(matches)
for i in matches:
    print(i)

pat="Sat, mat, pat, cat"
res=re.findall("[Smpc]at",pat) # this will collect all the pattern from the string 'pat' which ends with 'at' and starts with 'S','m','p'and'c' (specified through [Smpc]) !!
print(res)

res2=re.findall("[mp]at",pat) # this will collect all the pattern from the string 'pat' which ends with 'at' and starts with 'm' and 'p' (specified through [mp]) !!
print(res2)

res3=re.findall("[c-p]at",pat) # this will collect all the pattern from the string 'pat' which ends with 'at' and starting ranging from 'c' to 'p' (specified through [c-p]) !!
print(res3)

res3=re.findall("[^m-p]at",pat) # this will collect all the pattern from the string 'pat' which ends with 'at' and exclude the starting ranging from 'm' to 'p' (specified through [^m-p]) !!
print(res3) # Note: ^ is used to exclude specific pattern

# 2) search() --> this helps us to search for any pattern in the given text

String2="This is very nice tutorial for beginners!"

print(type(re.search("very",String2))) # it will print <class 're.Match'> , it is an object of class re.Match

if re.search("very",String2):
    print("It is present") 
else:
    print("Not Found!")

if re.search("Hello",String2):
    print("It is present") 
else:
    print("Not Found!")

ran="Here is \\akshat"
print(ran)
print(re.search(r"\\akshat",ran)) # it will print <re.Match object; span=(8, 15), match='\\akshat'>

# 3) finditer() --> this will give the starting and ending index of matched pattern in the given text(or string)

test2="He is very cool. He is awsome!"

for i in re.finditer("is",test2):
    tup=i.span() # this will make tuple 'tup' and put the starting and ending index in it!!
    print(tup)
    print(type(tup))

# 4) compile() and sub() 

t1=re.compile("is")
print(t1)

a1=re.sub("is","was",test2) # by this it will replace all "is" with "was"
print(a1)

a2=t1.sub("was",test2) # by this also it will replace all "is" with "was"
print(a2)

a3= re.sub("is","was",test2,1) # by this it will replace only one "is" with "was"
print(a3)

String3='''Hi!
How are You? '''

print(String3)

t2=re.compile("\n")
String3=t2.sub(" ",String3) # replacing "\n" with " "
print(String3)

# Difference between \d and \D
num="12345"
print("Matches",re.findall('\d',num)) # it give the list one digit numbers in the given string
print("Matches",re.findall('\d{5}',num)) # it will print ['12345']  
print("Matches",re.findall('\d{4}',num)) # it will print ['1234']   
print("Matches",re.findall('\D',num)) # it will print [] since \D means anything except numbers or [^0-9]

num1="123 1234 12345 123456 1234567"
print("Matches",re.findall('\d{5,7}',num1)) # it will print ['12345', '123456', '1234567'] ; i.e. those patterns which contain 5 to 7 length of digits!!

# Note: \w --> [a-zA-Z0-9] and \W --> [^a-zA-Z0-9]
# Note: \s --> [\f\n\r\t\v] ans \S --> [^\f\n\r\t\v]

# Example question --> Email verifier!! 
'''A valid Email should have :
1) 1 to 20 lowercase and uppercase letters, numbers 
2) @ symbol
3) 2 to 20 lowercase and uppercase letters, numbers
4) A period(.)
5) 2 to 3 lowercase and uppercase letters
'''
emails="akshat174@gmail.com lekhansh@.com"
print("Matched Emails!",re.findall("[\w]{1,20}@[\w]{2,20}.[A-Za-z]{2,3}",emails))
# Note: only "akshat174@gmail.com" will get printed!
