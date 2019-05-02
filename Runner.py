from Analysis import Analysis as Analysis

class Runner:
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
        return self.lastPerError, self.trainEndVal, self.testEndVal, self.lastDev

tickerList = ["AAPL"]
#tickerList = ["SBUX", "TSLA", "AAPL"]
#tickerList = ["SBUX", "TSLA", "AAPL", "BAC", "SNAP", "JPM", "MSFT", "AMZN", "CSCO", "F", "GE"]
#tickerList = ["SBUX", "TSLA", "AAPL", "BAC", "SNAP", "JPM", "MSFT", "AMZN", "CSCO", "F", "GE", "FISV", "XOM", "T", "NVDA", "INTC", "AMD"]

g = 0
b = 0
for ticker in tickerList: 
    # ticker, start index, training duration, testing duration, table, graph                    
    x = Runner(ticker, 200, 60, 20, False, False)
    
    train = x.getData()[1]
    test = x.getData()[2]
    
    change = test - train
    dev = x.getData()[3][1]
    
    if dev > 0 and change < 0:
        if abs(dev) > abs(change):
            print("Bad    " + ticker)
            b += 1
        if abs(dev) < abs(change):
            print("Good   " + ticker)
            g += 1
            
    elif dev < 0 and change > 0:
        if abs(dev) < abs(change):
            print("Good   " + ticker)
            g += 1
        if abs(dev) > abs(change):
            print("Bad    " + ticker)
            b += 1
            
    else:
        if abs(dev) < abs(change):
            print("Good   " + ticker)
            g += 1
        else:
            print("Bad    " + ticker)
            b += 1
print()
print(str(g / (g + b) * 100)[:7] + " % Good")

y = 0
for ticker in tickerList:                      
    x = Runner(ticker, 200, 60, 30, False, False)    
    y += abs(x.getData()[0][1])
    
y /= len(tickerList)
print(str(y)[:7]+" % Error Overall")

