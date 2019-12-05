

from EdgeStats import EdgeStats
import random
import numpy as np

class MCTSNode:

    
    def __init__(self, board, prob_of_chosen = 0,parent = None):
        self.board = board
        self.stats = EdgeStats(prob_of_chosen)
        self.parent = parent
        self.children = []

    def MakeMove(self,temperature):
        n_array = np.array([])
        for child in self.children:
            n_array = np.append(n_array,child.GetN())
        n_array_norm = n_array / n_array.sum()
        rand = random.uniform(0,1)
        pi = self.board.GetPi(n_array)
        index_of_pick = 0
        sum_probs = n_array_norm[index_of_pick]
        while rand > sum_probs:
            index_of_pick += 1
            sum_probs += n_array_norm[index_of_pick]
        #index_of_pick = np.argmax(n_array) if temperature = 0
        pick = self.children[index_of_pick]
        return (pick,self.board,pi)
        
    def getTotalN(self):
        sumN = 0
        for child in self.children:
            sumN += child.GetN()
        return sumN
    
        
    '''
    places board thrugh NN and gets prob dist of moves
    and gets probability of winning
    sets self.Children
    '''    
    def evaluate(self):
        #get the prio probabilities for
        #lists of boards and there probabilites of being chosen
        #all moves are possible
        boards, p, v = self.board.Evaluate()
        for board, probability in zip(boards,p):
            self.children.append(MCTSNode(board,probability,self))
        return v
    
    
    def CalculateQplusU(self,total_n):
        return self.stats.CalculateQplusU(total_n)
        
    def GetN(self):
        return self.stats.N
    
    def TerminalNode(self):
        return self.board.GameOver()
    
    '''
    only call this if TerminalNode is true
    '''
    def Result(self):
        return self.board.Value()
        
    '''
    select the next node to go to
    this is the argmax of Q + U
    '''
    #need to looks at when not expanded
    #need to look at when game is over
    def Select(self):
        #base cases
        if self.board.GameOver():
            vflipped = 1 - self.board.Value()
            self.stats.Update(vflipped)
            return vflipped
        
        if not self.children: #see if node is expanded
            vflipped = 1 - self.evaluate()
            self.stats.Update(vflipped)
            return vflipped
            
        all_counts =self.getTotalN()
        
        best_child = None
        best_score = -1
        for child in self.children:
            score = child.CalculateQplusU(all_counts)
            if score > best_score:
                best_score = score
                best_child = child
        v = best_child.Select()
        vflipped = 1 - v
        self.stats.Update(vflipped)
        return vflipped