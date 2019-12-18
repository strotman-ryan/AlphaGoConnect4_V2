#Player class for a human

from AbstractPlayer import AbstractPlayer


class AIPlayer(AbstractPlayer):
    
    def __init__(self, neuralNetworks, mcts,temperture, numRollouts):
        self.neuralNetworks = neuralNetworks
        self.mcts = mcts
        self.temperture = temperture
        self.numRollouts = numRollouts
    
    #returns column (0 -> columns -1) to make move in
    def MakeMove(self,gameState):
        self.mcts.SetRootNode(gameState)
        self.mcts.DoSearch(self.neuralNetworks, self.numRollouts)
        nextGameState, pi = self.mcts.ChooseMove(self.temperture)
        print(pi)
        return nextGameState, pi
        
        

