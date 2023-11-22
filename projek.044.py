num = int(input("How many friends do you want to invite to this party? "))
if num < 10:
    for i in range(0,num):
        name = input("Enter a name: ")
        print(name, "has been invited")
    else:
        print("to many people")