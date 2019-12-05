

#MCTS version 2
import math
import numpy as np
from TestBoard import TestBoard, NNforTest

class MCTS:
    
    '''
    this is the starting board
    # of times to run
    '''
    def __init__(self, board, num_rollouts = 200):
        self.root_node = Node(board)
        self.num_rollouts = num_rollouts
        
    #run the search for num_rollouts
    def DoSearch(self):
        for _ in range(self.num_rollouts):
            self.Select()
        pass
    
    '''
    find the next leaf node to expand
    '''
    def Select(self):
        self.root_node.Select()
        
    '''
    selects the move with the 
    1 -> vist dist
    0 -> max visit WARNING cannot do exactly 0
    '''
    def Play(self,temperature = 1):
        new_node,pre_board, pi = self.root_node.MakeMove(temperature)
        self.root_node = new_node
        return (pre_board, pi)
        


class Node:

    
    def __init__(self, board, prob_of_chosen = 0,parent = None):
        self.board = board
        self.stats = Stats(prob_of_chosen)
        self.parent = parent
        self.children = []

    def MakeMove(self,temperature):
        n_array = np.array([])
        for child in self.children:
            n_array = np.append(n_array,child.GetN())
        index_of_pick = np.argmax(n_array)
        pick = self.children[index_of_pick]
        pi = self.board.GetPi(n_array)
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
            self.children.append(Node(board,probability,self))
        return v
    
    
    def CalculateQplusU(self,total_n):
        return self.stats.CalculateQplusU(total_n)
        
    def GetN(self):
        return self.stats.N
        
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
        
        
        
class Stats:
    const = 1 #TODO chnage this
    
    def __init__(self,prob_of_chosen):
        self.N = 0
        self.W = 0
        self.P = prob_of_chosen
        self.Q = 0
        
    def addN(self):
        self.N += 1
    
    '''
    v is the probability of winning at the end of the roll out
    '''
    def updateW(self,v):
        self.W += v
    
    def calculateQ(self):
        self.Q =  self.W / self.N
    
    def Update(self,v):
        self.addN()
        self.updateW(v)
        self.calculateQ()
        
    def CalculateQplusU(self,total_n):
        return self.Q + Stats.const * self.P * math.sqrt(total_n) / (1 + self.N)
    
    
    
nn = NNforTest()
rootBoard = TestBoard(np.array([0,0,0,0]),nn)
mc = MCTS(rootBoard)
mc.DoSearch()
result = mc.Play()
     
    
    
    
    
    
    
    
    
    
    
    
        