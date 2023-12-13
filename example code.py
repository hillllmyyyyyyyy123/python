msg = input("masukan kata")
if msg.isupper():
    print("uppercase")
else:
    print("this is not uppercase")
if msg.islower():
    print("lowercase")
else:
    print("this is not lowercase")
msg = "Hello"
for letter in msg:
    print(letter,end="*")