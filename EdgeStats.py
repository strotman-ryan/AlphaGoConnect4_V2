
import math

class EdgeStats:
    const = 1 #TODO chnage this
    
    def __init__(self,prob_of_chosen):
        self.N = 0
        self.W = 0
        self.P = prob_of_chosen
        self.Q = 0
        
    def addN(self):
        self.N += 1
    
    '''
    v is the probability of winning at the end of the roll out
    '''
    def updateW(self,v):
        self.W += v
    
    def calculateQ(self):
        self.Q =  self.W / self.N
    
    def Update(self,v):
        self.addN()
        self.updateW(v)
        self.calculateQ()
        
    def CalculateQplusU(self,total_n):
        result = self.Q + EdgeStats.const * self.P * math.sqrt(total_n) / (1 + self.N)
        return result