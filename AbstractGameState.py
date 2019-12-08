

'''
abstract class for game_states, implement this for a new game
'''
from abc import ABC, abstractmethod 


class AbstractGameState(ABC):
    
    '''
    return array of next possible states
    return array of probabilities produced by NN and renormalized
    '''
    @abstractmethod
    def GetNextStatesWithProbabilites(self, neuralNetworks):
        pass
    
    '''
    returns true if end of game
    '''
    @abstractmethod
    def IsTerminal(self):
        pass
    
    '''
    returns what NN determines
    if a terminal node returns the value with respect to whos turn it is
    '''
    @abstractmethod
    def ProbabilityOfWinning(self,neuralNetworks):
        pass
    
    '''
    determines if two games states are the same
    return boolean
    '''
    @abstractmethod
    def IsSameAs(self, gameState):
        pass
    
    '''
    given the probilities of moves add in 0s where moves are impossible
    '''
    @abstractmethod
    def CompletePi(self, arrayOfProbabilites):
        pass
    
    '''
    return a value between [0,1] that determines the value of the end game with respct to current player
    '''
    @abstractmethod
    def ValueOfWinner(self):
        pass
    
    
    
    
    
    