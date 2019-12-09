
import numpy as np

from keras.models import Sequential, load_model
from keras.layers import Dense
from keras import losses
import pandas as pd

class DummyGameNN:
    
    def __init__(self):
        self.movesNN = DummyGameMoveNN()
        self.policyNN = DummyGamePolicyNN()

    def GetMoveProbabilities(self,gameState):
        board_rep = gameState.board
        return self.movesNN.Predict(np.array([self.translateBoardRep(board_rep.copy())]))

    def GetProbabilityOfWinning(self,gameState):
        board_rep = gameState.board
        return self.policyNN.Predict(np.array([self.translateBoardRep(board_rep.copy())]))  # need to make it (1,8)

    def Train(self,trainingExamples):
        results = np.array([])
        pis = np.array([[0,0,0,0]])
        boards = np.array([[0,0,0,0,0,0,0,0]])
        for example in trainingExamples:
            results = np.append(results, example.result)
            board = example.gameState.board
            board = self.translateBoardRep(board)
            boards = np.append(boards,[board], axis = 0)
            pis = np.append(pis, [example.pi], axis = 0)
        boards = np.delete(boards,0,0)
        pis = np.delete(pis,0,0)
        self.policyNN.Train(boards, results)
        self.movesNN.Train(boards,pis)

    def translateBoardRep(self, board_rep):
        board_rep_p1 = board_rep.copy()
        board_rep_p2 = board_rep.copy()
        board_rep_p1[board_rep_p1 != 1] = 0
        board_rep_p2[board_rep_p2 != -1] = 0
        return np.append(board_rep_p1, board_rep_p2) 
    
    def Save(self, fileName):
        fileNames = fileName.split()
        self.policyNN.Save(fileNames[0])
        self.movesNN.Save(fileNames[1])
    
    def Load(self, fileName):
        fileNames = fileName.split()
        self.policyNN.Load(fileNames[0])
        self.movesNN.Load(fileNames[1])

#produces probabilty of winning for whos turn it is
class DummyGamePolicyNN:
    
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units = 30, activation = 'relu', input_dim = 8))
        self.model.add(Dense(units = 1, activation = 'sigmoid'))
        self.model.compile(loss='mean_squared_error',optimizer='sgd',metrics=['accuracy'])
    
    def Predict(self, board_rep):
        return self.model.predict(board_rep)[0][0]

    def Train(self, board_reps, outcomes):
        self.model.fit(board_reps, outcomes, epochs = 20, batch_size = 50)
        
    def Save(self, fileName):
        fileName = fileName + '.h5'
        self.model.save(fileName)
    
    def Load(self, fileName):
        fileName = fileName + '.h5'
        self.model = load_model(fileName)

class DummyGameMoveNN:
    
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units = 30, activation = 'relu', input_dim = 8))
        self.model.add(Dense(units = 4, activation = 'softmax'))
        self.model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
        
    def Predict(self, board_rep):
        return self.model.predict(board_rep)[0]
    
    def Train(self, board_reps, pis):
        self.model.fit(board_reps,pis, epochs = 20, batch_size = 8)
        
    def Save(self, fileName):
        fileName = fileName + '.h5'
        self.model.save(fileName)
    
    def Load(self, fileName):
        fileName = fileName + '.h5'
        self.model = load_model(fileName)
    


        
        
      
        
        
        
        
        
        
        
        
        
