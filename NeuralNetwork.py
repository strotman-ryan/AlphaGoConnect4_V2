#Neural Network

from keras.models import Sequential
from keras.layers import Dense
from keras import losses


class NeuralNetwork:
    
    
    '''
    This model expects 84 inpu parameters that are zero or one
    the first 42 inputs are 1 if the first player has a piece there
    rotate throught the spots from left to right then top to bottom
    therefore the first input is 1 if player one has a peice in the top left column
    0 if player one is not there
    same for the last 42 inputs for plyer 2
    ex. the seventh input is 1 if player one has a piece in the top row and right most column
    '''
    def __init__(self):
        model = Sequential()
        model.add(Dense(units=100,activation='relu',input_dim=42 * 2))
        model.add(Dense(units=20,activation='relu'))
        model.add(Dense(units=7,activation='softmax'))
        model.compile(loss=losses.categorical_crossentropy,optimizer='sgd',metrics=['accuracy'])
        self.model = model
        
    '''
    expects an array of length 84 like described above
    returns the ditribution
    '''
    def MakePrediction(board_input):
        pass
    
    
    '''
    Xtrain is a 3d array of board states like described above
    Ytrain is a 2d array of what the ouputs should be
    '''
    def Train(Xtrain, Ytrain):
        pass
    
    '''
    saves this model
    '''
    def Save():
        pass
    
    '''
    loads a model
    '''
    def Load():
        pass
    
    
    
    
        