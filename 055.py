import random
num = random.randint(1,5)
guess = int(input("enter a number: "))
if guess == num:
    print("well done")
elif guess > num:
    print("too high")
    guess = int(input("guess againt: "))
    if guess == num:
        print("6")
        print("correct")
    else:
        print("you lose")
elif guess < num:
    print("too low")
    guess = int(input("guess again: "))
    if guess == num:
        print("correct")
    else:
        print("you lose")