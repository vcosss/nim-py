import numpy as np

# returns utility value
def utility(turn):
  ut = np.zeros(p)
  ut[(turn-1)%p] = 1
  print("utility:", ut)
  return ut

# returns boolean 
def is_leaf(rows):
  return np.sum(rows)==0

p = 3 # number of players
# turn indexing from 0

def max_val(rows,turn):
  print("curr",rows,"turn", turn)
  if is_leaf(rows):
    print("leafff")
    return utility(turn)
  res_val = -1000
  res = res_val * np.ones(p)
  print(rows)
  
  for i in range(len(rows)):
    c=1
    for j in range(1,rows[i]+1):
      row1 = rows.copy()
      row1[i] -= j
      res_temp = max_val(row1, (turn+1) % p)
      if res_val > res_temp[turn]:
        continue
      elif res_val < res_temp[turn]:
        res= res_temp
        res_val = res_temp[turn]
      else:
        print("gon for summ")
        res+=res_temp
        c+=1
      print("i",i,"j",j)
      print("res",res)
    res/=c
    print("res", res)
  return res
  
rows = np.array([1,2])
max_val(rows,0)