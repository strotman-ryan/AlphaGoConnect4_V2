#random AI

from AbstractPlayer import AbstractPlayer
import numpy as np
import random
'''
Will make a random turn each time that is within the rule set
'''
class RandomPlayer(AbstractPlayer):
    
    def __init__(self, random_seed = None):
        random.seed(random_seed)
    
    def MakeMove(self,board):
        legalMove = False
        column = -1
        numColumns = board.shape[1] - 1
        while(not legalMove):
            column = random.randint(0,numColumns)
            legalMove = np.any(np.where(board[:,column] == 0, True, False))
        return column