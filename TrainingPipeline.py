# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:35:45 2019

@author: strotman.7
"""
from DummyGameNN import DummyGameNN
from DummyGameType import DummyGameType
from Evaluator import Evaluator
from SelfPlay import SelfPlay
from AIPlayerFactory import AIPlayerFactory


class TrainingPipeline:
    
    def __init__(self, game, neuralNetwork):
        self.game = game
        self.neuralNetwork = neuralNetwork
        self.aiFactory = AIPlayerFactory()
    
    
    def Train(self):
        for _ in range(4):
            aiPlayer = self.aiFactory.GetSelfPlayAI(self.neuralNetwork)
            selfPlay = SelfPlay(aiPlayer, self.game)
            selfPlay.PlayGames(100)
            nn = DummyGameNN()
            nn.Train(selfPlay.GetData())
            evaluator = Evaluator(self.neuralNetwork, nn, self.game)
            if evaluator.IsNN2BetterThanNN1(100):
                print("replacing NN")
            self.neuralNetwork = nn
        self.neuralNetwork.Save("policy move")
        return self.neuralNetwork
    

pipeline = TrainingPipeline(DummyGameType(), DummyGameNN())
pipeline.Train()
        
nn = DummyGameNN()
nn.Load("policy move")