subject_list = ["maths","english","computing","history","science","spanish"]
print(subject_list)
dislike = input("which of these subjects do you dislike? ")
getrid = subject_list.index(dislike)
del subject_list.index[getrid]
print(subject_list)