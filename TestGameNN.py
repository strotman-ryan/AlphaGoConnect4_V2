
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras import losses
import pandas as pd

class TestGameNN:
    
    def __init__(self, policyNN):
        self.policyNN = policyNN
        #self.moveNN = moveNN
        return
    
    def GetProbabilities(self,board_rep):
        #throw into NN
        return np.array([.2,.2,.3,.3])
    
    def GetProbOfWinning(self,board_rep):
        prediction = self.policyNN.Predict(np.array([self.translateBoardRep(board_rep.copy())]))  # need to make it (1,8)
        #print(prediction)
        return prediction
    
    def Train(self,training_examples):
        results = np.array([])
        boards = np.array([[0,0,0,0,0,0,0,0]])
        for example in training_examples:
            results = np.append(results, example.result)
            board = example.board.board
            board = self.translateBoardRep(board)
            boards = np.append(boards,[board], axis = 0)
        boards = np.delete(boards,0,0)
        print(boards)
        self.policyNN.Train(results, boards)
    
    def translateBoardRep(self, board_rep):
        board_rep_p1 = board_rep
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
        print(board_reps)
        print(outcomes)
        self.model.fit(board_reps, outcomes, epochs = 20, batch_size = 50)
        
        
      
        
        
policy = PolicyNN()
x = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0]])
y = np.array([.4, 1])
policy.Train(x,y)  
        
        
        
        
        
        
        
        
        
