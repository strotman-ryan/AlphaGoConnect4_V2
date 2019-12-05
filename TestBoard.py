#board for Test Game

import numpy as np

        
        

#class to do everything for test game
#all arrays are numpy
class TestBoard:
    
    def __init__(self,rep_of_board, nn):
        self.nn = nn
        self.board = rep_of_board
        
    def Initilize(self):
        self.board = np.array([0,0,0,0])
    
    #returns a three tuple
    # list of next possible boards
    # list of probabilities to that move
    # probability of whos turn it is to win= x
    def Evaluate(self):
        probabilities = self.nn.GetProbabilities(self.board)
        probOfWinning = self.nn.GetProbOfWinning(self.board)
        boards, probabilities = self.DeterminePossibleMoves(probabilities)
        return (boards, probabilities,probOfWinning)
        
    def DeterminePossibleMoves(self, probabilites):
         probabilites = probabilites[self.board == 0]
         probabilites = probabilites / probabilites.sum() #renomalize
         boards = np.array([[1,1,1,1]])
         temp_board = self.board.copy()
         for _ in probabilites:
             index = (temp_board==0).argmax()
             board = self.board.copy()
             board[index] = self.WhosMove()
             temp_board[index] = self.WhosMove()
             boards = np.append(boards,[board], axis = 0)
             board = board.copy()   #deep copy
         
         boards = np.delete(boards,0,0)
         board_obj = [TestBoard(board, self.nn) for board in  boards]
         return (board_obj ,probabilites)
     
    def WhosMove(self):
        return 1 if self.board.sum() == 0 else -1
    
    def GameOver(self):
        first_two_spots = self.board[0:2]
        return sum(first_two_spots != 0) == 2
    
    #return one if you are looking at the board and won
    # zero otherwise
    # need to come back to this
    def Value(self):
        player = self.WhosMove()
        if not self.GameOver():
            print("ERROR")
            return -45
        first_two_spots = self.board[0:2]
        player1won = sum(first_two_spots == 1) == 2
        player2won = sum(first_two_spots == -1) == 2
        if player1won and player == 1:
            return 1
        if player2won and player == -1:
            return 1
        if player1won and player == -1:
            return 0
        if player2won and player == 1:
            return 0
        return .5  # tie
    
    def GetPi(self, n_array):
        n_array_norm = n_array / n_array.sum()
        for index in np.nonzero(self.board != 0)[0]:
            n_array_norm = np.insert(n_array_norm, index, 0)
        return n_array_norm
        
        
        
        

    




