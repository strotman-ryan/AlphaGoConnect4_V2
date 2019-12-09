# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:35:45 2019

@author: strotman.7
"""
from MCTS import MCTS
from DummyGameNN import PolicyNN, DummyGameNN, MoveNN
from AIPlayer import AIPlayer
from DummyGame import DummyGame
from Evaluator import Evaluator
from SelfPlay import SelfPlay


class TrainingPipeline:
    
    def __init__(self, game, neuralNetwork):
        self.game = game
        self.neuralNetwork = neuralNetwork
    
    
    def Train(self):
        for _ in range(1):
            aiPlayer = AIPlayer(self.neuralNetwork, MCTS(), 1)
            selfPlay = SelfPlay(aiPlayer, self.game)
            selfPlay.PlayGames(100)
            nn = DummyGameNN()
            nn.Train(selfPlay.GetData())
            evaluator = Evaluator(self.neuralNetwork, nn, self.game)
            if evaluator.IsNN2BetterThanNN1(100):
                print("replacing NN")
                self.neuralNetwork = nn
        return self.neuralNetwork
    

pipeline = TrainingPipeline(DummyGame(), DummyGameNN())
pipeline.Train()
        