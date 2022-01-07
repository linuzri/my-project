word = input("input: ")
size = len(word)
my_list = ["jan","feb","mac","apr"]

# sequence of numbers
for i in range(size):
    print(i, word[i])

# sequence of words
for j in word:
    print(j)

# sequence of list
for month in my_list:
    print(month)