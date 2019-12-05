

from MCTS import MCTS
from TestBoard import TestBoard
from TestGameNN import TestGameNN
import numpy as np
#make data
class SelfPlay:
    
    '''
    NN is NNforTest
    '''
    def __init__(self, NN, game, num_games = 100):
        self.nn = NN
        self.game = game
        self.num_games = num_games
        self.training_data = np.array([])
        
    def PlayGames(self):
        for _ in range(self.num_games):
            self.game.Initilize()
            self.playGame(MCTS(self.game))
        
        
    def playGame(self,mc):
        traning_examples = np.array([])
        while not mc.EndOfGame():
            mc.DoSearch()
            board, pi = mc.Play()
            traning_examples = np.append(traning_examples, TrainingExample(board, pi))
        result = mc.Result()
        for example in traning_examples:
            result = 1 - result
            example.AddResult(result)
        self.training_data = np.append(self.training_data,traning_examples)
        
        
class TrainingExample:
    
    def __init__(self, board, pi):
        self.board = board
        self.pi = pi
        
    def AddResult(self,result):
        self.result = result


nn = TestGameNN()
board = TestBoard(np.array([0,0,0,0]), nn)
sp = SelfPlay(nn, board)
sp.PlayGames()
'''
mc = MCTS(board)
mc.DoSearch()
play = mc.Play()
'''