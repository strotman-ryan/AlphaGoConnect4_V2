




#this class manages what data is used for training next


class DataManager:
    
    def __init__(self):
        self.dataGroupedByAI = []
        self.timesDataIsAdded = 0
    
    def InputData(self, data):
        self.timesDataIsAdded += 1
        self.dataGroupedByAI.append(data)
        if self.timesDataIsAdded > 10:
            self.dataGroupedByAI.pop(0)
    
    def GetTrainingData(self):
        data = []
        for dataAI in self.dataGroupedByAI:
            data.extend(dataAI)
        return data
    