import random
win_num=random.randint(1,100)   # generates any random integer between 1 and 100
user=int(input("Guess a Number between 1 to 100"))
if user==win_num:
    print("YOU WIN!")
else:   # nested if else
    if(user<win_num):
        print("Too Low!")
    else:
        print("Too High")
