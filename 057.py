import random
num = random.randint(1,10)
correct = False
while correct == False:
    guess = int(input("enter a number: "))
    if guess == num:
        correct = True
        print("6")
    elif guess > num:
        print("too high")
    else:
        print("too low")