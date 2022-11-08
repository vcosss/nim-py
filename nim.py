import random

game_flow = "n"
while game_flow == "n":

    print("PLAY A HUMAN VS. HUMAN NIM GAME\n")
    print("NOTE- The player to remove the last stick wins")
    print("NOTE- The rows are numbered 1, 2 and 3 respectively\n")

    player_1 = input("Enter player 1's name: ")
    player_2 = input("Enter player 2's name: ")
    turn = 0
    a, b, c = random.randint(10, 20), random.randint(10, 20), random.randint(10, 20)
    """row1-a
       row2-b
       row3-c"""

    print("")
    print(chr(11007) * a, " (", a, ")", sep="")
    print(chr(11007) * b, " (", b, ")", sep="")
    print(chr(11007) * c, " (", c, ")", sep="")
    print("")

    while True:

        if turn % 2 == 0:
            print(player_1.upper(), "'S TURN:", sep="")
            row = int(input("Enter the row to remove sticks: "))
            num = int(input("Enter how many sticks to remove: "))
        else:
            print(player_2.upper(), "'S TURN:", sep="")
            row = int(input("Enter the row to remove sticks: "))
            num = int(input("Enter how many sticks to remove: "))

        if row == 1 and a != 0:
            if num > a or num <= 0:
                print("\nINVALID NUMBER. Please enter a valid number.\n")
                continue
            a -= num
        elif row == 2 and b != 0:
            if num > b or num <= 0:
                print("\nINVALID NUMBER. Please enter a valid number.\n")
                continue
            b -= num
        elif row == 3 and c != 0:
            if num > c or num <= 0:
                print("\nINVALID NUMBER. Please enter a valid number.\n")
                continue
            c -= num
        else:
            print("\nINVALID ROW. Please enter valid row\n")
            continue

        print("")
        print(chr(11007) * a, " (", a, ")", sep="")
        print(chr(11007) * b, " (", b, ")", sep="")
        print(chr(11007) * c, " (", c, ")", sep="")
        print("")

        if a + b + c == 0:
            if turn % 2 == 0:
                print("\n", player_1.upper(), "!!! WON THE GAME !!!")
            else:
                print("\n", player_2.upper(), "!!! WON THE GAME !!!")
            break

        turn += 1

    print("\n", "-" * 70, "\n", end="", sep="")
    game_flow = input("\nEnter n to play a new game or press q to quit the game:")
    print("\n", "-" * 70, "\n", end="", sep="")
    print("-" * 70, "\n" * 2, end="")

print("THANK YOU! GOODBYE")
input("Press ENTER  to exit")
