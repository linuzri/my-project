list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# odd num % 2 == 0
# even num & 2 != 0

new_list = []

# odd numbers
for i in list1:
    if i % 2 != 0:
        new_list.append(i)
#print(new_list)

# even numbers
for j in list2:
    if j % 2 == 0:
        new_list.append(j)
#print(new_list)

print(f"New List : {new_list}")

