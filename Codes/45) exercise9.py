# we will generate an random integer and we will take input from user untill he/she guesses right number
import random
num=random.randint(1,100) # generates any random number between 1 to 100
c=0
for i in range(1,100):
    c+=1
    n=int(input("Guess a number: "))
    if n==num:
        print(f"You Won! You Guessed the number after {c} trials! ")
        break
    elif n<num:
        print("Too Low!")
    else:
        print("Too High!")

