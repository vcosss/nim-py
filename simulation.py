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


# engines_arr = [
#   [Dum(2,0),Maxn(2,1)],
#   [Dum(2,0),Paranoid(2,1)],
#   [Dum(2,0),MPmix(2,1)],
#   [Paranoid(2,0),Maxn(2,1)],
#   [Maxn(2,0),MPmix(2,1)],
#   [Paranoid(2,0),MPmix(2,1)],
# ]
# for i in tqdm(range(len(engines_arr)),desc="Simulating"):
#   print(simulate(200,engines_arr[i]))
  
# print("M R R R }| depth=3") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Maxn(4,3,max_depth=3,grow_depth=0)]))
# print("M R R R }| depth=5") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Maxn(4,3,max_depth=5,grow_depth=0)]))
# print("M R R R }| depth=7") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Maxn(4,3,max_depth=7,grow_depth=0)]))

# print("R R R P | depth=3") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Paranoid(4,3,max_depth=3,grow_depth=0)]))
# print("R R R P | depth=5") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Paranoid(4,3,max_depth=5,grow_depth=0)]))
# print("R R R P | depth=7") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Paranoid(4,3,max_depth=7,grow_depth=0)]))
# print("R R R P | depth=9") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Paranoid(4,3,max_depth=9,grow_depth=0)]))

# print("R R R M | growdepth=1")
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Maxn(4,3,grow_depth=1)]))
# print("R R R P | growdepth=1")
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Paranoid(4,3,grow_depth=1)]))

# print("R R R X | td=0.2 | to=0.2") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.2,thresh_off=0.2,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.2 | to=0.3") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.2,thresh_off=0.3,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.2 | to=0.4") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.2,thresh_off=0.4,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.3 | to=0.2") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.3,thresh_off=0.2,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.3 | to=0.3") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.3,thresh_off=0.3,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.3 | to=0.4") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.3,thresh_off=0.4,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.4 | to=0.2") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.4,thresh_off=0.2,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.4 | to=0.3") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.4,thresh_off=0.3,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.4 | to=0.4") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.4,thresh_off=0.4,max_depth=5,grow_depth=0)]))

# print("R R R X | td=0.2 | to=0.3 | depth=3 | grow_depth=0") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.2,thresh_off=0.3,max_depth=3,grow_depth=0)]))
# print("R R R X | td=0.2 | to=0.3 | depth=5 | grow_depth=0") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.2,thresh_off=0.3,max_depth=5,grow_depth=0)]))
# print("R R R X | td=0.2 | to=0.3 | depth=7 | grow_depth=0") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.2,thresh_off=0.3,max_depth=7,grow_depth=0)]))
# print("R R R X | td=0.2 | to=0.3 | grow_depth=1") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,thresh_def=0.2,thresh_off=0.3,grow_depth=1)]))

# M: growdepth = 1
# P: depth = 7 | growdepth = 0
# X: td = 0.2 | to = 0.3 | depth = 7 | grow_depth = 0

# print("R R R M1}| heuristic=1 | grow_depth=1") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Maxn(4,3,heuristic_type=1,grow_depth=1)]))
# print("R R R M2}| heuristic=2 | grow_depth=1") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Maxn(4,3,heuristic_type=2,grow_depth=1)]))
# print("R R R P1}| heuristic=1 | max_depth=7 |grow_depth=0") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Paranoid(4,3,heuristic_type=1,max_depth=7,grow_depth=0)]))
# print("R R R P2}| heuristic=2 | max_depth=7 |grow_depth=0") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),Paranoid(4,3,heuristic_type=2,max_depth=7,grow_depth=0)]))
# print("R R R X1}| heuristic=1 | td=0.2 | to=0.3 | max_depth=7 |grow_depth=0") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,heuristic_type=1,thresh_def=0.2,thresh_off=0.3,max_depth=7,grow_depth=0)]))
# print("R R R X2}| heuristic=2 | td=0.2 | to=0.3 | max_depth=7 |grow_depth=0") 
# print(simulate(100,[Dum(4,0),Dum(4,1),Dum(4,2),MPmix(4,3,heuristic_type=2,thresh_def=0.2,thresh_off=0.3,max_depth=7,grow_depth=0)]))

# print("M2 M2 X1 M2}") 
# print(simulate(100,[
#   Maxn(4,0,heuristic_type=2,grow_depth=1),
#   Maxn(4,1,heuristic_type=2,grow_depth=1),
#   MPmix(4,2,heuristic_type=1,thresh_def=0.2,thresh_off=0.3,max_depth=7,grow_depth=0),
#   Maxn(4,3,heuristic_type=2,grow_depth=1)]))
# print("P1 P1 X1 P1}") 
# print(simulate(100,[
#   Paranoid(4,0,heuristic_type=1,max_depth=7,grow_depth=0),
#   Paranoid(4,1,heuristic_type=1,max_depth=7,grow_depth=0),
#   MPmix(4,1,heuristic_type=1,thresh_def=0.2,thresh_off=0.3,max_depth=7,grow_depth=0),
#   Paranoid(4,3,heuristic_type=1,max_depth=7,grow_depth=0)]))
# print("M1 M1 M2")
# print(simulate(100,[
#   Maxn(4,0,heuristic_type=1,grow_depth=1),
#   Maxn(4,1,heuristic_type=1,grow_depth=1),
#   Maxn(4,2,heuristic_type=2,grow_depth=1)]))
# print("M2 M1 R")
# print(simulate(100 ,[
#   Maxn(4,0,heuristic_type=2,grow_depth=1),
#   Maxn(4,1,heuristic_type=1,grow_depth=1),
#   Dum(4,2)]))

