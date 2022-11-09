import numpy as np

def is_leaf(rows):
  """returns true if leaf node"""
  return np.sum(rows) == 0

def utility(turn,root_turn,p):
  """returns utility value for a given state"""
  return int(turn == (root_turn+1)%p)
  
def heuristic(rows,turn,root_turn,p):
  """returns heuristic value for a given state"""
  maxv = np.sum(rows)
  minv = np.count_nonzero(rows)
  
  a = (minv+turn-1)%p
  b = (maxv+turn-1)%p
  
  jump = root_turn-a
  if jump<0:
    jump += p
    
  return ((maxv-(minv+jump))//p)/(maxv-minv+1)

def paranoid(rows,turn,p):
  res, best_row, best_sticks = max_val(rows,p,turn,turn)
  return (best_row,best_sticks)

def max_val(rows,p,turn,root_turn,max_depth=7,depth=0):
  if is_leaf(rows) or depth>=max_depth:
    # print("leafff")
    return heuristic(rows,turn,root_turn,p), -1, -1
      
  res_val = -1000
  best_row,best_sticks = 1,1
  for i in range(len(rows)):
    for j in range(1, rows[i] + 1):
      res_temp,bla1,bla2 = min_val(rows,p,(turn + 1) % p,root_turn,max_depth,depth+1)
      if res_val < res_temp:
        res_val = res_temp
        best_row = i+1
        best_sticks = j
  return res_val,best_row,best_sticks


def min_val(rows,p,turn,root_turn,max_depth=5,depth=0):
  if is_leaf(rows) or depth>=max_depth:
    # print("leafff")
    return heuristic(rows,turn,root_turn,p), -1, -1
      
  res_val = 1000
  best_row,best_sticks = 1,1
  for i in range(len(rows)):
    for j in range(1, rows[i] + 1):
      if turn==root_turn:
        res_temp,bla1,bla2 = max_val(rows,p,(turn + 1) % p,root_turn,max_depth,depth+1)
      else:  
        res_temp,bla1,bla2 = min_val(rows,p,(turn + 1) % p,root_turn,max_depth,depth+1)
      if res_val > res_temp:
        res_val = res_temp
        best_row = i+1
        best_sticks = j
  return res_val,best_row,best_sticks
        