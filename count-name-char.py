myname = input("Name: ")
count = 0

for i in myname:
    if i == " ":
        continue
    else:
        count += 1

print(count)