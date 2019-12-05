

#MCTS version 2
import numpy as np
from TestBoard import TestBoard
from MCTSNode import MCTSNode

class MCTS:
    
    '''
    this is the starting board
    # of times to run
    '''
    def __init__(self, board, num_rollouts = 10):
        self.root_node = MCTSNode(board)
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
    
    '''
    returns true if root node is in an end state
    '''
    def EndOfGame(self):
        return self.root_node.TerminalNode()
    
    def Result(self):
        return self.root_node.Result()
        



        
        
        

    
      
    
    
    
    
    
    
    
    
    
    
    
        