#Player class for a human

from AbstractPlayer import AbstractPlayer


class AIPlayer(AbstractPlayer):
    num_rollouts = 30
    temperature = 1
    
    def __init__(self, neuralNetworks, mcts):
        self.neuralNetworks = neuralNetworks
        self.mcts = mcts
    
    #returns column (0 -> columns -1) to make move in
    def MakeMove(self,gameState):
        self.mcts.SetRootNode(gameState)
        self.mcts.DoSearch(self.neuralNetworks, AIPlayer.num_rollouts)
        nextGameState, pi = self.mcts.ChooseMove(AIPlayer.temperature)
        return nextGameState, pi
        
        

