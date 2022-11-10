import numpy as np

class Engine:

    def __init__(self, num_players, p_num, max_depth=5):
        self.num_players = num_players
        self.p_num = p_num
        self.max_depth = max_depth

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

    def __init__(self, num_players, p_num, max_depth=None):
        super().__init__(num_players, p_num, max_depth)

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
                    heur[j] += 1
            
        return heur/np.sum(heur)

    def choose(self,rows):
        _, best_row, best_sticks = self.max_val(rows,self.p_num)
        return (best_row, best_sticks)
    
    def max_val(self,rows,turn,depth=0):
        '''returns best move for a given state'''
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

    def __init__(self, num_players, p_num, max_depth=None, pruning=None):
        super().__init__(num_players, p_num, max_depth)
        self.pruning = pruning

    def utility(self,turn):
        '''returns utility array for leaf node'''
        return int(turn == (self.p_num+1)%self.num_players)

    def heuristic(self,rows,turn):
        '''returns heuristic value for a given state'''
        maxv = np.sum(rows)
        minv = np.count_nonzero(rows)
            
        a = (minv+turn-1)%self.num_players
        b = (maxv+turn-1)% self.num_players
        
        jump = self.p_num-a
        if jump<0:
            jump += self.num_players
            
        return ((maxv-(minv+jump))//self.num_players)/(maxv-minv+1)
    
    def choose(self,rows):
        _, best_row, best_sticks = self.max_val(rows,self.p_num,-1000,1000)
        return (best_row, best_sticks)

    def max_val(self,rows,turn,alpha,beta,depth=0):
        '''returns best move for a given state'''
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

                if (turn==self.p_num):
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
    

class Dum(Engine):
    
    def __init__(self, num_players, p_num, max_depth=None):
        super().__init__(num_players, p_num, max_depth)

    def choose(self,rows):
        '''returns best move for a given state'''
        row = np.random.choice(np.argwhere(rows>0).reshape(-1)) + 1
        sticks = np.random.choice(np.arange(1,rows[row-1]+1))
        return (row, sticks)


class Human:
        
    def __init__(self, num_players, p_num, max_depth=None):
        super().__init__(num_players, p_num, max_depth)
    
    def choose(self,rows):
        '''returns best move for a given state'''
        row = int(input("Enter row number: "))
        sticks = int(input("Enter number of sticks: "))
        return (row, sticks)
