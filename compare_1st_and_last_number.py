def compare_first_and_last_num(numberlist):
    firstnumber = numberlist[0]
    lastnumber = numberlist[-1]

    if firstnumber == lastnumber:
        return True
    else:
        return False

given_num = [10, 33, 67, 23, 50, 40, 70]
print(compare_first_and_last_num(given_num))

#print(given_num[0])
#print(given_num[-1])
