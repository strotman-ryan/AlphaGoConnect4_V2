

import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Conv2D, Flatten
from keras import losses

from AbstractNeuralNetwork import AbstractNeuralNetwork



class Connect4NNConvo(AbstractNeuralNetwork):
    
    def __init__(self):
        self.winNN = Connect4WinNNConvo()
        self.movesNN = Connect4MovesNNConvo()
        
    def GetMoveProbabilites(self, gameState):
        #TODO
        return [.1,.1,.1,.1,.1,.1,.4]
    
     def GetProbabilityOfWinning(self, gameState):
         pass
     
    def Train(self, trainingExamples):
        pass
    
     def Save(self, fileName):
         pass
        
     def Load(self, fileName):
         pass
       
        
class Connect4WinNNConvo:
    
    def __init__(self):
        self.model =Sequential()
        self.model.add(Conv2D(30,kernel_size=(4,4), activation='relu', input_shape=(6,7,2)))
        self.model.add(Flatten())
        self.model.add(Dense(60, activation='relu'))
        self.model.add(Denses(1, activation='sigmoid'))
        self.model.compile(loss = 'mean_squared_error', optimizer = 'sgd', metrics = ['accuracy'])
    
    def Predict(self, board_rep):
        self.model.predict(board_rep)
    
    def Train(self, board_reps, outcomes):
        pass
    
    def Save(self, fileName):
        fileName = fileName + '.h5'
        self.model.save(fileName)
        
    def Load(self, fileName):
        fileName = fileName + '.h5'
        self.model = load_model(fileName)
    
    
class Connect4MovesNNConvo:
    
    def __init__(self):
        pass
    
    
    
    def Save(self, fileName):
        fileName = fileName + '.h5'
        self.model.save(fileName)
        
    def Load(self, fileName):
        fileName = fileName + '.h5'
        self.model = load_model(fileName)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    