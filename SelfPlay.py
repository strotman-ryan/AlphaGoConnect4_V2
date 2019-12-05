

from MCTS_v2 import MCTS
from TestBoard import TestBoard, NNforTest

#make data
class SelfPlay:
    
    '''
    NN is NNforTest
    '''
    def __init__(self, NN, num_games = 100):
        self.nn = NN
        self.num_games = num_games
        
        
    def playGame(self):
        pass
        




