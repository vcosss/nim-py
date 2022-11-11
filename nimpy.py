import numpy as np

class Engine:

    def __init__(self, num_players, p_num, heuristic_type=1, max_depth=5, grow_depth=1):
        self.num_players = num_players
        self.p_num = p_num
        self.max_depth = 3 if grow_depth else max_depth
        self.heuristic_type = heuristic_type
        self.grow_depth = grow_depth
        self.depth_values = {15:5, 10:7}

    def utility(self, rows):
        pass

    def heuristic(self, rows):
        pass

    def is_leaf(self,rows):
        '''returns true if leaf node'''
        return np.sum(rows) == 0

    def choose(self,rows):
        pass
    
    def max_val(self,rows):
        pass

    def min_val(self,rows):
        pass
    
class Maxn(Engine):

    def __init__(self, num_players, p_num,heuristic_type=1, max_depth=5, grow_depth=0):
        super().__init__(num_players, p_num,heuristic_type, max_depth, grow_depth)

    def utility(self,turn):
        '''returns utility array for leaf node'''
        util = np.zeros(self.num_players)
        util[(turn - 1) % self.num_players] = 1
        return util

    def heuristic(self,rows,turn):
        '''returns heuristic value for a given state'''
        
        maxv = np.sum(rows)
        minv = np.count_nonzero(rows)
        heur = np.zeros(self.num_players)
        
        for j in range(self.num_players):
            for i in range(minv, maxv+1):
                if j == ((i+turn-1)%self.num_players):
                    heur[j] += (1) if self.heuristic_type==1 else (-32 + np.log(i) * 36)
            
        return heur/np.sum(heur)
        
    def choose(self,rows):
        _, best_row, best_sticks = self.max_val(rows,self.p_num)
        return (best_row, best_sticks)
    
    def max_val(self,rows,turn,depth=0):
        '''returns best move for a given state'''
        if self.grow_depth:
            for k in self.depth_values.keys():
                if np.sum(rows) <= k:
                    self.max_depth = self.depth_values[k]
                    break                
            
        if self.is_leaf(rows):
            return self.utility(turn),-1,-1
            
        if (self.max_depth and depth>=self.max_depth):
            return self.heuristic(rows,turn),-1,-1

        curr = -1000
        max_arr = np.zeros(self.num_players)
        best_row,best_sticks = 1,1
    
        for row in range(len(rows)):
            c_eq = 1    # count of equal children
            for sticks in range(1, rows[row] + 1):
                new_rows = rows.copy()
                new_rows[row] -= sticks
                arr,_,_ = self.max_val(new_rows,(turn+1)%self.num_players,depth+1)
                if arr[turn] > curr:
                    curr = arr[turn]
                    max_arr = arr
                    best_row,best_sticks = row+1,sticks
                elif arr[turn] == curr:
                    max_arr += arr
                    c_eq+=1

        return max_arr/c_eq,best_row,best_sticks

class Paranoid(Engine):

    def __init__(self, num_players, p_num,heuristic_type=1, max_depth=5, pruning=True, grow_depth=1):
        super().__init__(num_players, p_num, heuristic_type,max_depth, grow_depth)
        self.pruning = pruning

    def utility(self,turn):
        '''returns utility array for leaf node'''
        return int(turn == (self.p_num+1)%self.num_players)
    
    def heuristic(self,rows,turn):
        maxv = np.sum(rows)
        minv = np.count_nonzero(rows)
        heur = 0

        for i in range(minv, maxv+1):
            if self.p_num == ((i+turn-1)%self.num_players):
                heur += (1) if self.heuristic_type==1 else (-32 + np.log(i) * 36)
        
        return (heur/(maxv-minv+1)) if self.heuristic==1 else (np.sum(-32 + np.log(np.arange(minv, maxv+1)) * 36)) 
           
    def choose(self,rows):
        _, best_row, best_sticks = self.max_val(rows,self.p_num,-1000,1000)
        return (best_row, best_sticks)

    def max_val(self,rows,turn,alpha,beta,depth=0):
        '''returns best move for a given state'''
        if self.grow_depth:
            for k in self.depth_values.keys():
                if np.sum(rows) <= k:
                    self.max_depth = self.depth_values[k]
                    break   
        
        if self.is_leaf(rows):
            return self.utility(turn),-1,-1
            
        if (self.max_depth and depth>=self.max_depth):
            return self.heuristic(rows,turn),-1,-1

        maxv = -1000
        best_row,best_sticks = 1,1
        for row in range(len(rows)):
            for sticks in range(1, rows[row]+1):
                new_rows = rows.copy()
                new_rows[row] -= sticks

                curr,_,_ = self.min_val(new_rows,(turn+1)%self.num_players,alpha,beta,depth+1)
               
                if curr > maxv:
                    maxv = curr
                    best_row,best_sticks = row+1,sticks
                if self.pruning:
                    if maxv >= beta:
                        return maxv,best_row,best_sticks
                    alpha = max(alpha,maxv)

        return maxv,best_row,best_sticks

    def min_val(self,rows,turn,alpha,beta,depth=0):
        '''returns best move for a given state'''
        if self.grow_depth:
            for k in self.depth_values.keys():
                if np.sum(rows) <= k:
                    self.max_depth = self.depth_values[k]
                    break   
        
        if self.is_leaf(rows):
            return self.utility(turn),-1,-1
            
        if (self.max_depth and depth>=self.max_depth):
            return self.heuristic(rows,turn),-1,-1

        minv = 1000
        best_row,best_sticks = 1,1
        for row in range(len(rows)):
            for sticks in range(1, rows[row]+1):
                new_rows = rows.copy()
                new_rows[row] -= sticks

                if ((turn+1)%self.num_players==self.p_num):
                    curr,_,_ = self.max_val(new_rows,(turn+1)%self.num_players,alpha,beta,depth+1)
                else:
                    curr,_,_ = self.min_val(new_rows,(turn+1)%self.num_players,alpha,beta,depth+1)
                
                if curr < minv:
                    minv = curr
                    best_row,best_sticks = row+1,sticks
                if self.pruning:
                    if minv <= alpha:
                        return minv,best_row,best_sticks
                    beta = min(beta,minv)

        return minv,best_row,best_sticks

class Offensive(Engine):
    
    def __init__(self, num_players, p_num, heuristic_type=1, max_depth=3, grow_depth=1):
        super().__init__(num_players, p_num,heuristic_type,  max_depth, grow_depth)

    def utility(self,turn):
        '''returns utility array for leaf node'''
        util = np.zeros(self.num_players)
        util[(turn - 1) % self.num_players] = 1
        return util

    def heuristic(self,rows,turn):
        '''returns heuristic value for a given state'''
        
        maxv = np.sum(rows)
        minv = np.count_nonzero(rows)
        heur = np.zeros(self.num_players)
        
        for j in range(self.num_players):
            for i in range(minv, maxv+1):
                if j == ((i+turn-1)%self.num_players):
                    heur[j] += (1) if self.heuristic_type==1 else (-32 + np.log(i) * 36)
            
        return heur/np.sum(heur)

    def choose(self,rows,target_num):
        self.target_num = target_num
        _, best_row, best_sticks = self.min_val(rows,self.p_num)
        return (best_row, best_sticks)
    
    def min_val(self,rows,turn,depth=0):
        '''returns best move for a given state'''
        if self.grow_depth:
            for k in self.depth_values.keys():
                if np.sum(rows) <= k:
                    self.max_depth = self.depth_values[k]
                    break   
        
        if self.is_leaf(rows):
            return self.utility(turn),-1,-1
            
        if (self.max_depth and depth>=self.max_depth):
            return self.heuristic(rows,turn),-1,-1

        curr = 1000
        min_arr = np.zeros(self.num_players)
        best_row,best_sticks = 1,1
    
        for row in range(len(rows)):
            c_eq = 1    # count of equal children
            for sticks in range(1, rows[row] + 1):
                new_rows = rows.copy()
                new_rows[row] -= sticks
                
                arr,_,_ = self.max_val(new_rows,(turn+1)%self.num_players,depth+1)
                
                if arr[self.target_num] < curr:
                    curr = arr[self.target_num]
                    min_arr = arr
                    best_row,best_sticks = row+1,sticks
                elif arr[self.target_num] == curr:
                    min_arr += arr
                    c_eq+=1

        return min_arr/c_eq,best_row,best_sticks
    
    def max_val(self,rows,turn,depth=0):
        '''returns best move for a given state'''
        if self.grow_depth:
            for k in self.depth_values.keys():
                if np.sum(rows) <= k:
                    self.max_depth = self.depth_values[k]
                    break   
        
        if self.is_leaf(rows):
            return self.utility(turn),-1,-1
            
        if (self.max_depth and depth>=self.max_depth):
            return self.heuristic(rows,turn),-1,-1

        curr = -1000
        max_arr = np.zeros(self.num_players)
        best_row,best_sticks = 1,1
    
        for row in range(len(rows)):
            c_eq = 1    # count of equal children
            for sticks in range(1, rows[row] + 1):
                new_rows = rows.copy()
                new_rows[row] -= sticks
                if ((turn+1)%self.num_players==self.p_num):
                    arr,_,_ = self.min_val(new_rows,(turn+1)%self.num_players,depth+1)
                else:
                    arr,_,_ = self.max_val(new_rows,(turn+1)%self.num_players,depth+1)
                if arr[turn] > curr:
                    curr = arr[turn]
                    max_arr = arr
                    best_row,best_sticks = row+1,sticks
                elif arr[turn] == curr:
                    max_arr += arr
                    c_eq+=1

        return max_arr/c_eq,best_row,best_sticks

class MPmix(Engine):
    
    def __init__(self, num_players, p_num, heuristic_type=1, max_depth=3, grow_depth=1, thresh_def=0.3, thresh_off=0.3):
        super().__init__(num_players, p_num,heuristic_type,  max_depth, grow_depth)
        self.maxn = Maxn(num_players, p_num, max_depth)
        self.para = Paranoid(num_players, p_num, max_depth)
        self.off = Offensive(num_players, p_num, max_depth)
        self.thresh_def = thresh_def
        self.thresh_off = thresh_off

    def heuristic(self,rows,turn):
        '''returns heuristic value for a given state'''
        
        maxv = np.sum(rows)
        minv = np.count_nonzero(rows)
        heur = np.zeros(self.num_players)
        
        for j in range(self.num_players):
            for i in range(minv, maxv+1):
                if j == ((i+turn-1)%self.num_players):
                    heur[j] += (1) if self.heuristic_type==1 else (-32 + np.log(i) * 36)
            
        return heur/np.sum(heur)

    def choose(self,rows):
        '''returns best move for a given state'''
        heur = self.heuristic(rows,self.p_num)
        heur = np.sort(heur)[::-1]
        leading_edge = heur[0] - heur[1]
        leader = np.argmax(heur)
        if (leader == self.p_num):
            if (leading_edge > self.thresh_def):
                return self.para.choose(rows)
        else:
            if (leading_edge > self.thresh_off):
                return self.off.choose(rows,leader)
        return self.maxn.choose(rows)

class Dum(Engine):
    
    def __init__(self, num_players, p_num, heuristic_type= None, max_depth=3, grow_depth=0):
        super().__init__(num_players, p_num, heuristic_type, max_depth, grow_depth)

    def choose(self,rows):
        '''returns best move for a given state'''
        row = np.random.choice(np.argwhere(rows>0).reshape(-1)) + 1
        sticks = np.random.choice(np.arange(1,rows[row-1]+1))
        return (row, sticks)


class Human(Engine):
        
    def __init__(self, num_players, p_num, heuristic_type = None, max_depth=3, grow_depth=0):
        super().__init__(num_players, p_num, heuristic_type,max_depth, grow_depth)
    
    def choose(self,rows):
        '''returns best move for a given state'''
        row = int(input("Enter row number: "))
        sticks = int(input("Enter number of sticks: "))
        return (row, sticks)
        