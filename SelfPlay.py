# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:45:27 2019

@author: strotman.7
"""
import numpy as np
from TrainingGame import TrainingGame
from MCTS import MCTS
from DummyGameNN import PolicyNN, DummyGameNN, MoveNN
from AIPlayer import AIPlayer
from DummyGame import DummyGame

class SelfPlay:
    
    
    def __init__(self, player, game):
        self.game = game
        self.player = player
        self.trainingExamples = np.array([])
        
    def PlayGames(self, numGames):
        for _ in range(numGames):  
            initilizedGame = TrainingGame(self.player, self.game)
            initilizedGame.PlayGame()
            self.trainingExamples = np.append(self.trainingExamples, initilizedGame.GetTraingData())
    
    def GetData(self):
        return self.trainingExamples

  
nn = DummyGameNN(PolicyNN(), MoveNN())
for _ in range(6):
    aiPlayer = AIPlayer(nn, MCTS())
    selfPlay = SelfPlay(aiPlayer, DummyGame())
    selfPlay.PlayGames(1000)
    nn.Train(selfPlay.GetData())


