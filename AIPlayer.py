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
        #self.mcts.PrintTree()
        nextGameState, pi = self.mcts.ChooseMove(self.temperture)
        return nextGameState, pi
    
    def SetTemperature(self, new_temperature):
        self.temperture = new_temperature
        
        

