import matplotlib.pyplot as plt
from prettytable import PrettyTable

class DataVisualization:
    def createTickerLable(ticker):
        print()    
        sepLine = ""
        for ii in range(0,len(ticker)+6):
            sepLine += "#"
                
        print(sepLine)
        print("## "+ticker+" ##")
        print(sepLine)

    def createTable():        
        table = PrettyTable()
        table.field_names = ["METHOD", "AVG. DEV.", "PER. ERROR", "1DAY DEV.", "1DAY PER. ERROR", "END DEV.", "END PER. ERROR", "PRICE"]
            
        return table
        
    def displayTable(table):
        print()
        print(table)
        
    def graphDataAll(training, pred, test, ticker, label, reg):
        for element in test:
            training.append(element)
        
        realX = range(1, len(training) + 1)
        predX = range(len(realX) - len(test) + 1, len(realX) + 1)
        
        fig1, ax1 = plt.subplots()
        
        ax1.plot(predX, pred, color="blue")
        ax1.plot(realX, training, color="red")    
        ax1.legend(["Predicted", "Real"])    

        ax1.set_xlabel('Day Number')
        ax1.set_ylabel('Stock Value')
        ax1.set_title('Predicted vs Real Data (All) (' + ticker + ') (' + label.upper() + ') (' + reg + ')')
        fig1.show()
        
    def graphDataResults(pred, test, ticker, label, reg):
        x = range(1, len(test) + 1)
        
        fig2, ax2 = plt.subplots()
        
        ax2.plot(x, pred, color="blue")
        ax2.plot(x, test, color="red")    
        ax2.legend(["Predicted", "Real"])    

        ax2.set_xlabel('Day Number')
        ax2.set_ylabel('Stock Value')
        ax2.set_title('Predicted vs Real Data (Results) (' + ticker + ') (' + label.upper() + ') (' + reg + ')')
        fig2.show()