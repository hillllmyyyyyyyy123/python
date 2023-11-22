import random
num = random.randint(1,10)
correct = False
while correct == False:
    guess = int(input("enter a number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print(5)
        print("too higt")
    else:
        print("too low")