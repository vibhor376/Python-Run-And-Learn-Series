# our task is to define a function which tells us whether the given string is palindrome or not
# Palindrome - a string which reads same from both starting and end
def is_palindrome(text):
    return text==text[::-1]
n=input("Enter a string: ")
print(is_palindrome(n))