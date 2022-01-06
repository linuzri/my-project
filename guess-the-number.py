''' guess number game '''
import random

while True:
    choices = ["1", "2", "3"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Guess a number between 1 to 3 ? : ")

    if player == computer:
        print("computer guess : " + computer)
        print("you guess : " + player)
        print("you guessed right!")
    else:
        print("computer guess : " + computer)
        print("you guess : " + player)
        print("you missed!")

    play_again = input("play again (y/n) ? :")
    if play_again != 'y':
        break
print("bye")
