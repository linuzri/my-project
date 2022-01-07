def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 5] == 'Emmah'
    return count

count = count_emma("Emmah is good developer. Emmah is a writer")
print("Emma appeared ", count, "times")