import numpy as np

def utility(turn,p):
    """returns utility array for leaf node"""
    ut = np.zeros(p)
    ut[(turn - 1) % p] = 1
    # print("utility:", ut)
    return ut, -1,-1

def is_leaf(rows):
    """returns true if leaf node"""
    return np.sum(rows) == 0

# turn indexing from 0
def maxn(rows, turn,p):
    """returns best move for a given state"""
    res,best_row,best_sticks = max_val(rows, turn,p)
    # print("besti", besti, "bestj", bestj)
    return (best_row,best_sticks)

def max_val(rows, turn,p):
    # print("curr", rows, "turn", turn)
    if is_leaf(rows):
        # print("leafff")
        return utility(turn,p)
    res_val = -1000
    res = res_val * np.ones(p)
    # print(rows)
    best_row,best_sticks = 1,1

    for i in range(len(rows)):
        c = 1
        for j in range(1, rows[i] + 1):
            new_rows = rows.copy()
            new_rows[i] -= j
            res_temp,bla1,bla2 = max_val(new_rows, (turn + 1) % p,p)
            # print("res_temp", res_temp)
            if res_val > res_temp[turn]:
                continue
            elif res_val < res_temp[turn]:
                best_row,best_sticks = i+1,j
                res = res_temp
                res_val = res_temp[turn]
            else:
                # print("gon for summ")
                res += res_temp
                c += 1
            # print("i", i, "j", j)
            # print("res", res)
        res /= c
        # print("res", type(res))
    return res,best_row,best_sticks

if __name__ == "__main__":
    rows = np.array([1, 2])
    max_val(rows, 0,3)
