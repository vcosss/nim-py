import numpy as np
import maxn
import paranoid
import os

def print_rows():
    os.system("cls")
    print("")
    for i in range(r):
        print(chr(11007) * rows[i], " (", rows[i], ")", sep="")
    print("")

def get_human_inputs():
    row = int(input("Enter the row to remove sticks: "))
    num = int(input("Enter how many sticks to remove: "))
    return row,num

def get_ai_inputs():
    row,num = paranoid.paranoid(rows, turn,p)
    return row,num

def print_utility():
    res = maxn.heuristic1(rows,turn,p)
    resp = paranoid.heuristic(rows,turn,turn,p)
    print(f"The current utility is {res[0]}, {resp}")

print("PLAY A MULTIPLAYER NIM GAME\n")
print("NOTE- The player to remove the last stick wins")
p = int(input("Enter number of human players: "))  # number of players
r = int(input("Enter number of rows: "))  # number of rows
rows = np.random.choice(range(3, 15), size=(r))

turn = 0
p+=1
while True:

    print_rows()
    print_utility()
    if turn == p - 1:
        print("AI's turn:")
        row,num = get_ai_inputs()
        print(f"AI chooses to remove {num} sticks from row {row}")
        input("Press enter to continue...")
    else:
        print(f"PLAYER {turn + 1}'S TURN:", sep="")
        row,num = get_human_inputs()

    if row <= r and rows[row - 1] != 0:
        if num > rows[row - 1] or num <= 0:
            print("\nINVALID NUMBER. Please enter a valid number.\n")
            continue
        rows[row-1] -= num
    else:
        print("\nINVALID ROW. Please enter valid row\n")
        continue
        
    if np.sum(rows) == 0:
        print_rows()
        res_string = "AI" if turn==p-1 else f"PLAYER {turn+1}"
        print(res_string, " WINS!", sep="")
        break

    turn = (turn+1)%p
