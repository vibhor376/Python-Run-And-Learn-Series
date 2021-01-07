# A list is a collection of data 
numbers=[1,2,3,4,5]  # list declaration syntax and it is list of integers
print(numbers)
words=["word1",'word2',"word3"] # list of strings as you can see we can use both '' and ""
print(words)
mixed=[1,2,3,4,"Five",'Six',7.0,None]  # Here the list contains integers, strings, float and None data types 
print(mixed)

# accessing list elements(Remember the indexing start from 0)
print(numbers[2])   
print(words[0])
print(mixed[6])
print(numbers[:2])
print(words[:])
print(mixed[4:])

# updating list elements
mixed[1]=8
print(mixed)
mixed[1:]="two"  # whole list will replace from index 1 to end
print(mixed)
mixed[1:]=["one","two"]
print(mixed)