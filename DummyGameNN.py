
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras import losses
import pandas as pd

class DummyGameNN:
    
    def __init__(self, policyNN, movesNN):
        self.movesNN = movesNN
        self.policyNN = policyNN
        return

    def GetProbabilities(self,board_rep):
        return self.movesNN.Predict(np.array([self.translateBoardRep(board_rep.copy())]))

    def GetProbOfWinning(self,board_rep):
        return self.policyNN.Predict(np.array([self.translateBoardRep(board_rep.copy())]))  # need to make it (1,8)

    def Train(self,training_examples):
        results = np.array([])
        pis = np.array([[0,0,0,0]])
        boards = np.array([[0,0,0,0,0,0,0,0]])
        for example in training_examples:
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

#produces probabilty of winning for whos turn it is
class PolicyNN:
    
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units = 30, activation = 'relu', input_dim = 8))
        self.model.add(Dense(units = 1, activation = 'sigmoid'))
        self.model.compile(loss='mean_squared_error',optimizer='sgd',metrics=['accuracy'])
    
    def Predict(self, board_rep):
        return self.model.predict(board_rep)[0][0]

    def Train(self, board_reps, outcomes):
        self.model.fit(board_reps, outcomes, epochs = 20, batch_size = 50)

class MoveNN:
    
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units = 30, activation = 'relu', input_dim = 8))
        self.model.add(Dense(units = 4, activation = 'softmax'))
        self.model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
        
    def Predict(self, board_rep):
        return self.model.predict(board_rep)[0]
    
    def Train(self, board_reps, pis):
        print(pis)
        self.model.fit(board_reps,pis, epochs = 20, batch_size = 8)
    


        
        
      
        
        
        
        
        
        
        
        
        
