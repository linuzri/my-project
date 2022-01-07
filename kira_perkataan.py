perkataan = input("Huruf untuk dikira : ")
kiraan = 0

for i in perkataan:
    if i == ' ':
        continue
    else:
        kiraan += 1

print(f"Perkataan '{perkataan}' mengandungi : {kiraan} huruf")