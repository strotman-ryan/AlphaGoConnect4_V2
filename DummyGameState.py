#board for Test Game

import numpy as np
from AbstractGameState import AbstractGameState

#this is one board state in the game and a series of methods
class DummyGameState(AbstractGameState):
    
    def __init__(self,rep_of_board):
        self.board = rep_of_board
        
    #returns a three tuple
    # list of next possible boards
    # list of probabilities to that move
    # probability of whos turn it is to win= x
    def GetNextStatesWithProbabilites(self,neuralNetworks):
        probabilities = neuralNetworks.GetProbabilities(self.board)
        return self.determinePossibleMoves(probabilities)
    
    
    def IsTerminal(self):
        first_two_spots = self.board[0:2]
        return sum(first_two_spots != 0) == 2
    
    #return one if you are looking at the board and won
    # zero otherwise
    # need to come back to this
    def ProbabilityOfWinning(self,neuralNetworks):
        if not self.IsTerminal():
            return neuralNetworks.GetProbOfWinning(self.board)
        print("Error")

    
    
    def ValueOfWinner(self):
        if not self.IsTerminal():
            print("Error")
            return
        player = self.whosMove()
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
    
    
    def CompletePi(self, arrayOfProbabilites):
        for index in np.nonzero(self.board != 0)[0]:
            arrayOfProbabilites = np.insert(arrayOfProbabilites, index, 0)
        return arrayOfProbabilites
    
    def IsSameAs(self, gameState):
        pass
        
    def determinePossibleMoves(self, probabilites):
         probabilites = probabilites[self.board == 0]
         probabilites = probabilites / probabilites.sum() #renomalize
         
         boards = np.array([[1,1,1,1]])
         temp_board = self.board.copy()
         for _ in probabilites:
             index = (temp_board==0).argmax()
             board = self.board.copy()
             board[index] = self.whosMove()
             temp_board[index] = self.whosMove()
             boards = np.append(boards,[board], axis = 0)
         
         boards = np.delete(boards,0,0)
         board_obj = [DummyGameState(board) for board in  boards]
         return (board_obj ,probabilites)
     
        
    def whosMove(self):
        return 1 if self.board.sum() == 0 else -1
     
     

        

        

    




