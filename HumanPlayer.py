#Player class for a human

from AbstractPlayer import AbstractPlayer


class HumanPlayer(AbstractPlayer):
    
    def __init__(self):
        return
    
    #returns column (0 -> columns -1) to make move in
    def MakeMove(self,board):
        return int(input("Input a column 0-6: "))
