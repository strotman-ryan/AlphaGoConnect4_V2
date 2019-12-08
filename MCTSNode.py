

from EdgeStats import EdgeStats
import random
import numpy as np
random.seed(0) 
class MCTSNode:
    
    
    def __init__(self, gameState, prob_of_chosen = 0):
        self.gameState = gameState
        self.stats = EdgeStats(prob_of_chosen)
        self.children = []

    '''
    temperature [.1,1]
    '''
    def ChooseMove(self,temperature):
        n_array = self.getVisitCounts()
        n_array_temperature = np.power(n_array,1/temperature)
        pi_missing_data = n_array_temperature / n_array_temperature.sum()
        rand = random.uniform(0,1)
        index_of_pick = 0
        sum_probs = pi_missing_data[index_of_pick]
        while rand > sum_probs:
            index_of_pick += 1
            sum_probs += pi_missing_data[index_of_pick]
        pick = self.children[index_of_pick]
        pi = self.gameState.CompletePi(pi_missing_data)
        return (pick,pi)
    
        '''
    select the next node to go to
    this is the argmax of Q + U
    '''
    #need to looks at when not expanded
    #need to look at when game is over
    def Select(self, neuralNetworks):
        #base cases
        if self.gameState.IsTerminal():
            vflipped = 1 - self.gameState.ValueOfWinner()
            self.stats.Update(vflipped)
            return vflipped
        
        if not self.children: #see if node is expanded
            self.evaluate(neuralNetworks)
            vflipped = 1 - self.gameState.ProbabilityOfWinning(neuralNetworks)
            self.stats.Update(vflipped)
            return vflipped
            
        all_counts =self.getVisitCounts().sum()
        
        best_child = None
        best_score = -1
        for child in self.children:
            score = child.CalculateQplusU(all_counts)
            if score > best_score:
                best_score = score
                best_child = child
        v = best_child.Select(neuralNetworks)
        
        vflipped = 1 - v
        self.stats.Update(vflipped)
        return vflipped
        
    
    def getVisitCounts(self):
        n_array = np.array([])
        for child in self.children:
            n_array = np.append(n_array,child.stats.N)
        return n_array
    
        
    '''
    places board thrugh NN and gets prob dist of moves
    and gets probability of winning
    sets self.Children
    '''    
    def evaluate(self,neuralNetworks):
        gameStates, moveProbs = self.gameState.GetNextStatesWithProbabilites(neuralNetworks)
        for gameState, probability in zip(gameStates,moveProbs):
            self.children.append(MCTSNode(gameState,probability))
    
    
    def CalculateQplusU(self,total_n):
        return self.stats.CalculateQplusU(total_n)
        
    
        
