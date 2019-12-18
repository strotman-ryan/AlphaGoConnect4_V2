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
    load_str = "NN"
    
    def __init__(self, gameType):
        self.gameType = gameType
        self.neuralNetwork = gameType.GetOldNeuralNetwork(TrainingPipeline.load_str)
        self.aiFactory = AIPlayerFactory()
    
    
    def Train(self):
        counter = 0
        for _ in range(20):
            aiPlayer = self.aiFactory.GetSelfPlayAI(self.neuralNetwork)
            selfPlay = SelfPlay(aiPlayer, self.gameType)
            selfPlay.PlayGames(1)
            nn = self.gameType.GetNewNeuralNetwork()
            nn.Train(selfPlay.GetData())
            evaluator = Evaluator(self.neuralNetwork, nn, self.gameType)
            if evaluator.IsNN2BetterThanNN1(6):
                print("replacing NN")
                self.neuralNetwork = nn
                counter += 1
            self.neuralNetwork.Save(TrainingPipeline.load_str)
        print(counter)
        return self.neuralNetwork
    

pipeline = TrainingPipeline(Connect4GameType())
pipeline.Train()
        
