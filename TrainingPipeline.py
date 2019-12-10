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
from Connect4GameType import Connect4GameType


class TrainingPipeline:
    
    def __init__(self, gameType):
        self.gameType = gameType
        self.neuralNetwork = gameType.GetNewNeuralNetwork()
        self.aiFactory = AIPlayerFactory()
    
    
    def Train(self):
        for _ in range(4):
            aiPlayer = self.aiFactory.GetSelfPlayAI(self.neuralNetwork)
            selfPlay = SelfPlay(aiPlayer, self.gameType)
            selfPlay.PlayGames(30)
            nn = self.gameType.GetNewNeuralNetwork()
            nn.Train(selfPlay.GetData())
            evaluator = Evaluator(self.neuralNetwork, nn, self.gameType)
            if evaluator.IsNN2BetterThanNN1(8):
                print("replacing NN")
                self.neuralNetwork = nn
            self.neuralNetwork.Save("policy move")
        return self.neuralNetwork
    

pipeline = TrainingPipeline(Connect4GameType())
pipeline.Train()
        
nn = DummyGameNN()
nn.Load("policy move")