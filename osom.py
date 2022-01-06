''' permainan osom '''

import random

while True:
    pilihan = ["burung","batu","air"]
    komputer = random.choice(pilihan)
    pemain = None

    while pemain not in pilihan:
        pemain = input("burung,batu,air?: ").lower()

    if pemain == komputer:
        print("komputer :",komputer)
        print("pemain :",pemain)
        print("Seri!")
    elif pemain == "burung":
        if komputer == "batu":
            print("komputer :", komputer)
            print("pemain :", pemain)
            print("Anda kalah!")
        if komputer == "air":
            print("komputer :", komputer)
            print("pemain :", pemain)
            print("Anda menang!")
    elif pemain == "batu":
        if komputer == "air":
            print("komputer :", komputer)
            print("pemain :", pemain)
            print("Anda kalah!")
        if komputer == "burung":
            print("komputer :", komputer)
            print("pemain :", pemain)
            print("Anda menang!")
    elif pemain == "air":
        if komputer == "batu":
            print("komputer :", komputer)
            print("pemain :", pemain)
            print("Anda kalah!")
        if komputer == "burung":
            print("komputer :", komputer)
            print("pemain :", pemain)
            print("Anda menang!")

    main_semula = input("ingin main semula ? (ya/tidak)? : ").lower()
    if main_semula != "ya":
        break
print("bye!")