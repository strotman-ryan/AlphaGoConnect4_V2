import numpy as np

from Connect4GameState import Connect4GameState
from AbstractGameType import AbstractGameType
from Connect4NN import Connect4NN

class Connect4GameType(AbstractGameType):
    
    def __init__(self):
        pass
    
    '''
	Returns an empty representation of the game
	'''
    def GetStartingBoard(self):
        rows = 6
        columns = 7
        board = []
        for row in range(rows):
            new_row = []
            for column in range(columns):
                new_row.append(0)
            board.append(new_row)
        return Connect4GameState(board)
        #return Connect4GameState(np.zeros((rows,columns)))
    
    
    def GetOldNeuralNetwork(self, loadString):
        try: 
            nn = Connect4NN()
            nn.Load(loadString)
            return nn
        except:
            return self.GetNewNeuralNetwork()
    
    def GetNewNeuralNetwork(self):
        return Connect4NN()
'''
board = Connect4GameType().GetStartingBoard()
print(board)
'''