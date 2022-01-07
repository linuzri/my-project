'''
str_x = "Hello my name is Nazri. Nazri likes python programming!"
x = str_x.count("Nazri")
print(x)
'''

str_x = "Emma is good developer. Emma is a writer"
str_split = str_x.split(" ")
str_len = len(str_split)

count = 0
for i in range(0,str_len):
    if str_split[i] == "Emma":
        count = count + 1
    else:
        continue
print(f"Words 'Emma' = {count}")