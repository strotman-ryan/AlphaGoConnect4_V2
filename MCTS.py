

#MCTS version 2
from MCTSNode import MCTSNode

class MCTS:
    
    '''
    this is the starting board
    # of times to run
    '''
    def __init__(self):
        self.root_node = None
  
    '''
    TODO should search for children of rootnode but easy implementaion hear
    '''
    def SetRootNode(self, gameState):
        self.root_node = MCTSNode(gameState)
        
        
    #run the search for num_rollouts
    def DoSearch(self,neuralNetworks,numRollouts):
        for _ in range(numRollouts):
            self.root_node.Select(neuralNetworks)
    

    '''
    selects the move with the 
    1 -> vist dist
    0 -> max visit WARNING cannot do exactly 0
    '''
    def ChooseMove(self,temperature = 1):
        new_node, pi = self.root_node.ChooseMove(temperature)
        self.root_node = new_node
        return (new_node.gameState, pi)

       



        
        
        

    
      
    
    
    
    
    
    
    
    
    
    
    
        