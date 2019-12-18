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
from DataManager import DataManager


class TrainingPipeline:
    load_str = "NN2"
    
    def __init__(self, gameType):
        self.gameType = gameType
        self.neuralNetwork = gameType.GetOldNeuralNetwork(TrainingPipeline.load_str)
        self.aiFactory = AIPlayerFactory()
        self.dataManager = DataManager()
    
    
    def Train(self):
        counter = 0
        for _ in range(20):
            print("Iteraction: " + str(_))
            aiPlayer = self.aiFactory.GetSelfPlayAI(self.neuralNetwork)
            selfPlay = SelfPlay(aiPlayer, self.gameType)
            selfPlay.PlayGames(10)
            nn = self.gameType.GetNewNeuralNetwork()
            self.dataManager.InputData(selfPlay.GetData())
            nn.Train(self.dataManager.GetTrainingData())
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
        
