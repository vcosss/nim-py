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
        row, sticks = engines[turn].choose(rows)
        if verbose:
            print_rows(rows)
            print("Player {} chose row {} and {} sticks".format(turn+1, row, sticks))
        rows[row-1] -= sticks

        if np.sum(rows) == 0:
            if verbose:
                print(f"Player {turn+1} wins!")
                return turn
        turn = (turn+1)%len(engines)

# n = int(input("Enter number of players: "))
# print("-"*30)
# print("Enter the options in the format: <engine> <param1> <param2> ...")
# print("Params are optional and have a default value")
# print("The available options and params for the engines are:\n")
# print("Human        : H")
# print("Random Agent : R")
# print("Maxn Agent   : M [max_depth(int): default 5]")
# print("Paranoid     : P [max_depth(int): default 5] [pruning(bool): default 1]")
# print("-"*30)
# for i in range(n):
#   eng = input(f"Enter engine for player {i+1}: ")
  


swara = Maxn(4,3,heuristic_type = 1,max_depth=5)
icebear = Maxn(4,1,heuristic_type = 2,max_depth=5)
vcos = Maxn(4,2,heuristic_type = 2,max_depth=5)
space = Dum(4,0)
# space = MPmix(4,3,heuristic_type = 2,alpha = 0.4,0.175)
rows = np.random.choice(range(3, 15), size=(3))
play_game([space,icebear,vcos, swara],verbose=True,rows=rows)