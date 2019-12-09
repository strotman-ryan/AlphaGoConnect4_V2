#Player class for a human

from AbstractPlayer import AbstractPlayer


class HumanPlayer(AbstractPlayer):
    
    def __init__(self):
        return
    
    #returns column (0 -> columns -1) to make move in
    def MakeMove(self,gameState):
        return (gameState.GetNextStateFromHuman(), 0)
