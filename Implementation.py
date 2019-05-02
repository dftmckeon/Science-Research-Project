from Analysis import Analysis as Analysis

class Implementation:
    def __init__(self, ticker, start, training, test, table, graph):
        data = Analysis(ticker, start, training, test, table, graph)
        values = data.getData()
        
        self.regType = values[0]    # Regression Type
        self.dev = values[1]
        self.perError = values[2]
        self.oneDev = values[3]
        self.onePerError = values[4]
        self.lastDev = values[5]
        self.lastPerError = values[6]
        self.trainEndVal = values[7]
        self.testEndVal = values[8]
    
    def getData(self):
        return self.regType, self.dev, self.perError, self.oneDev, self.onePerError, \
                self.lastDev, self.lastPerError, self.trainEndVal, self.testEndVal