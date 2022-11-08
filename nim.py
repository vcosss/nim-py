import random
import numpy as np

game_flow = "n"
while game_flow == "n":

    print("PLAY A HUMAN VS. HUMAN NIM GAME\n")
    print("NOTE- The player to remove the last stick wins")
    p = int(input("Enter number of players: "))  # number of players
    r = int(input("Enter number of rows: "))  # number of rows
    turn = 0
    rows = np.random.choice(range(3, 15), size=(r))

    print("")
    for i in range(r):
        print(chr(11007) * rows[i], " (", rows[i], ")", sep="")
    print("")

    while True:

        print(turn % p + 1, "'S TURN:", sep="")
        row = int(input("Enter the row to remove sticks: "))
        num = int(input("Enter how many sticks to remove: "))

        if row <= r and rows[row-1] != 0:
            if num > rows[row-1] or num <= 0:
                print("\nINVALID NUMBER. Please enter a valid number.\n")
                continue
            rows[row-1] -= num

        else:
            print("\nINVALID ROW. Please enter valid row\n")
            continue

        print("")
        for i in range(r):
            print(chr(11007) * rows[i], " (", rows[i], ")", sep="")
        print("")

        if np.sum(rows) == 0:
            print(turn % p + 1, "WINS!", sep="")
            break

        turn += 1

    print("\n", "-" * 70, "\n", end="", sep="")
    game_flow = input(
        "\nEnter n to play a new game or press q to quit the game:")
    print("\n", "-" * 70, "\n", end="", sep="")
    print("-" * 70, "\n" * 2, end="")

print("THANK YOU! GOODBYE")
input("Press ENTER  to exit")
