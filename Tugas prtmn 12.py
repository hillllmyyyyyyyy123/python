word = input("enter a word")
leng = len(word)
num = 1
for x in word:
    position = leng - num
    letter = word[position]
    print(letter)
    num = num + 1