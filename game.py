import numpy as np
from nimpy import *

def print_rows(rows):
    # os.system("cls")
    print("")
    for i in range(len(rows)):
        print(chr(11007) * rows[i], " (", rows[i], ")", sep="")
    print("")

def play_game(engines, rows, verbose=False):
    turn = 0
    while True:
        print("\n"+"-"*30)
        print(f"PLAYER {turn+1}'S TURN")
        row, sticks = engines[turn].choose(rows)
        
        if row <= len(rows) and rows[row - 1] != 0:
            if sticks > rows[row - 1] or sticks <= 0:
                print("\nINVALID NUMBER. Please enter a valid number.\n")
                continue
            rows[row-1] -= sticks
        else:
            print("\nINVALID ROW. Please enter valid row\n")
            continue
            
        if verbose:
            print_rows(rows)
            print(f"Player {turn+1} chose {sticks} sticks from row {row}\n")

        if np.sum(rows) == 0:
            if verbose:
                print("="*30)
                print(f"\nPLAYER {turn+1} WINS!")
                return turn
        turn = (turn+1)%len(engines)

print("\nWELCOME TO MULTIPLAYER NIM GAME\n")
print("-"*30)
print("")
print("Enter the options in the format: <engine> <param1> <param2> ...")
print("Params are optional and have a default value")
print("The available options and params for the engines are:\n")
print("Human        : H")
print("Random Agent : R")
print("Maxn Agent   : M [max_depth(int): default 5] [heuristic_type(int): default 1] [grow_depth(bool): default 0]")
print("Paranoid     : P [max_depth(int): default 5] [heuristic_type(int): default 1] [grow_depth(bool): default 0] [pruning(bool): default 1]")
print("MPmix        : X [max_depth(int): default 5] [heuristic_type(int): default 1] [grow_depth(bool): default 0] [pruning(bool): default 1]")
print("")
print("-"*100)
print("")
n = int(input("Enter number of players: "))
players = []
for i in range(n):
    eng = input(f"Enter engine for player {i+1}: ")
    eng_split = eng.split(' ')
    if eng_split[0] == "H":
        players.append(Human(n, i))
    elif eng_split[0] == "R":
        players.append(Dum(n, i))
    elif eng_split[0] == "M":
        if len(eng_split)==2:
            players.append(Maxn(n, i, int(eng_split[1])))
        elif len(eng_split)==3:
            players.append(Maxn(n, i, int(eng_split[1]), int(eng_split[2])))
        elif len(eng_split)==4:
            players.append(Maxn(n, i, int(eng_split[1]), int(eng_split[2]), int(eng_split[3])))
        else:
            players.append(Maxn(n, i))
    elif eng_split[0] == "P":
        if len(eng_split)==2:
            players.append(Paranoid(n, i, int(eng_split[1])))
        elif len(eng_split)==3:
            players.append(Paranoid(n, i, int(eng_split[1]), int(eng_split[2])))
        elif len(eng_split)==4:
            players.append(Paranoid(n, i, int(eng_split[1]), int(eng_split[2]), int(eng_split[3])))
        elif len(eng_split)==5:
            players.append(Paranoid(n, i, int(eng_split[1]), int(eng_split[2]), int(eng_split[3]), int(eng_split[4])))
        else:
            players.append(Paranoid(n, i))
    elif eng_split[0] == "X":
        if len(eng_split)==2:
            players.append(MPmix(n, i, int(eng_split[1])))
        elif len(eng_split)==3:
            players.append(MPmix(n, i, int(eng_split[1]), int(eng_split[2])))
        elif len(eng_split)==4:
            players.append(MPmix(n, i, int(eng_split[1]), int(eng_split[2]), int(eng_split[3])))
        elif len(eng_split)==5:
            players.append(MPmix(n, i, int(eng_split[1]), int(eng_split[2]), int(eng_split[3]), int(eng_split[4])))
        else:
            players.append(MPmix(n, i))
             
print()      
print("-"*30)
r = int(input("Enter number of rows: "))  # number of rows
print("-"*30)
rows = np.random.choice(range(3, 15), size=r, replace=False)
print_rows(rows)

print(players)
play_game(players, rows, verbose=True)
