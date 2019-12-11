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
        return Connect4GameState(np.zeros((rows,columns)))
    
    
    def GetOldNeuralNetwork(self, loadString):
        try: 
            nn = Connect4NN()
            nn.Load(loadString)
            return nn
        except:
            return self.GetNewNeuralNetwork()
    
    def GetNewNeuralNetwork(self):
        return Connect4NN()