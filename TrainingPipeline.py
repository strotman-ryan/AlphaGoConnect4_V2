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
from twilio.rest import Client


client = Client("AC9c71e8bf50be8e734ed0d3c3ab855eb9", "62309c663d49dbc94a25d034ec176b5e")

class TrainingPipeline:
    load_str = "NN3"
    
    def __init__(self, gameType):
        self.gameType = gameType
        self.neuralNetwork = gameType.GetOldNeuralNetwork(TrainingPipeline.load_str)
        self.aiFactory = AIPlayerFactory()
        self.dataManager = DataManager()
    
    
    def Train(self):
        counter = 0
        for _ in range(50):
            print("Iteraction: " + str(_))
            aiPlayer = self.aiFactory.GetSelfPlayAI(self.neuralNetwork)
            selfPlay = SelfPlay(aiPlayer, self.gameType)
            selfPlay.PlayGames(10)
            self.dataManager.InputData(selfPlay.GetData())
            better = False
            nnsTrained = 0
            while not better and nnsTrained < 5:
                nnsTrained += 1
                nn = self.gameType.GetNewNeuralNetwork()
                nn.Train(self.dataManager.GetTrainingData())
                evaluator = Evaluator(self.neuralNetwork, nn, self.gameType)
                if evaluator.IsNN2BetterThanNN1(10):
                    print("replacing NN")
                    better = True
                    self.neuralNetwork = nn
                    counter += 1
            self.neuralNetwork.Save(TrainingPipeline.load_str)
        print(counter)
        client.messages.create(to="+15136384300", 
                       from_="+13345106249", 
                       body="Training Finished. The NN updated " + str(counter) + " times")
        return self.neuralNetwork
    

pipeline = TrainingPipeline(Connect4GameType())
pipeline.Train()
        
