from game import *
from nimpy import *
import numpy as np
from tqdm import tqdm

def simulate(n,engines):
  wins = {i:0 for i in range(len(engines))} 
  for i in tqdm(range(n),desc=f"Simulating"):
    winner = play_game(engines, np.random.choice(range(3, 10), size=3), verbose=False)
    wins[winner]+=1
  return wins

engines_arr = [[Dum(2,0),Maxn(2,1)],
              [Maxn(2,0),Dum(2,1)],
              [Dum(2,0),Paranoid(2,1)],
              [Paranoid(2,0),Dum(2,1)],
              [Dum(2,0),MPmix(2,1)],
              [MPmix(2,0),Dum(2,1)],
              [Maxn(2,0),Paranoid(2,1)],
              [Paranoid(2,0),Maxn(2,1)],
              [Maxn(2,0),MPmix(2,1)],
              [MPmix(2,0),Maxn(2,1)],
              [Paranoid(2,0),MPmix(2,1)],
              [MPmix(2,0),Paranoid(2,1)]]
  
for i in tqdm(range(len(engines_arr)),desc="Simulating"):
  s = simulate(100,engines_arr[i])
  print(s)

# for i in tqdm(range(100),desc=f"Simulating"):
#   val = play_game(engines_arr[0], np.random.choice(range(3, 10), size=3), verbose=False)
#   print(i,val)