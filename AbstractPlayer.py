#abstract class for all players

import abc

'''
the base class of all players
'''
class AbstractPlayer(abc.ABC):
    
    @abc.abstractmethod
    def MakeMove(self, gameState):
        pass