import numpy as np

from Connect4GameState import Connect4GameState
from AbstractGameType import AbstractGameType

class Connect4GameType(AbstractGameType):
    
    def __init__(self):
        pass
    
    '''
	Returns an empty representation of the game
	'''
	def GetStartingBoard():
		rows = 6
		columns = 7
		return Connect4GameState(np.zeros((rows,columns)))
    
    
    def GetNewNeuralNetwork():
        print("Need to implement this")