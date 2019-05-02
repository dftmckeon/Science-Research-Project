'''
    Predictive Modeling for the Stock Market
    10/2/2018
    Daniel McKeon

'''
import numpy as np

from StockData import StockData
from Regressions import Regressions as Reg
from DataComparison import DataComparison as DataComp
from DataVisualization import DataVisualization as DataVis

class Analysis():  
    
    def __init__(self, ticker, startDate, trainingDuration, testDuration, table, graph):
        self.table = table
        self.graph = graph
        self.ticker = ticker
        
        self.regType = ["POLY REG", "FFT"]
        self.dev = []
        self.perError = []
        self.oneDev = []
        self.onePerError = []
        self.lastDev = []
        self.lastPerError = []
        self.trainEndVal = 0
        self.testEndVal = 0
        
        if self.table:
            DataVis.createTickerLable(ticker)
        
        csv = ticker+".csv"
        
        training = StockData(csv, startDate, trainingDuration).data
        test = StockData(csv, startDate + trainingDuration, testDuration).data
        
        self.trainEndVal = training["adjust"][len(training)-1]
        self.testEndVal = test["adjust"][len(test)-1]
        
        self.dataProcessing(training, test)
        
    def dataProcessing(self, training, test):
        table = DataVis.createTable()
        
        typeList = ["adjust"]
        
        ##############################
        ### Polynomial Regression ###
        #############################
        for polyType in typeList:
            # Regressions
            coeffs = Reg.polyReg(training["day"], training[polyType])
            f = np.poly1d(coeffs)
            
            # Predicted Prices
            pred = f(test["day"]).tolist()
            
            # Average Deviation & Average Percent Error of Predicted Test Prices
            dev = DataComp.averageDev(pred, test[polyType])
            perError = DataComp.averagePerError(pred, test[polyType])
            oneDev = DataComp.dayOneAccuracy(pred, test[polyType])[0]
            onePerError = DataComp.dayOneAccuracy(pred, test[polyType])[1]
            lastDev = DataComp.lastDayAccuracy(pred, test[polyType])[0]
            lastPerError = DataComp.lastDayAccuracy(pred, test[polyType])[1]

            self.dev.append(dev)
            self.perError.append(perError)
            self.oneDev.append(oneDev)
            self.onePerError.append(onePerError)  
            self.lastDev.append(lastDev)
            self.lastPerError.append(lastPerError)
            
            '''
            if self.graph:
                DataVis.graphDataAll(training[polyType], pred, test[polyType], self.ticker, polyType, "POLY REG")
                #DataVis.graphDataResults(pred, test[polyType], self.ticker, polyType, "POLY-REG")
            '''
            
            # Add Row
            table.add_row(["POLY REG", str(dev)[:7], str(perError)[:7], str(oneDev)[:7], str(onePerError)[:7], str(lastDev)[:7], str(lastPerError)[:7], polyType.upper()])

        ##############################
        ### Fast Fourier Transform ###
        ############################## 
        for polyType in typeList:   
            # Regressions & Predicted Prices
            pred = Reg.fastFourier(training[polyType], test["day"]).tolist()[len(training[polyType]):]
                        
            # Average Deviation & Average Percent Error of Predicted Test Prices
            dev = DataComp.averageDev(pred, test[polyType])
            perError = DataComp.averagePerError(pred, test[polyType])
            oneDev = DataComp.dayOneAccuracy(pred, test[polyType])[0]
            onePerError = DataComp.dayOneAccuracy(pred, test[polyType])[1]     
            lastDev = DataComp.lastDayAccuracy(pred, test[polyType])[0]
            lastPerError = DataComp.lastDayAccuracy(pred, test[polyType])[1]

            self.dev.append(dev)
            self.perError.append(perError)
            self.oneDev.append(oneDev)
            self.onePerError.append(onePerError)  
            self.lastDev.append(lastDev)
            self.lastPerError.append(lastPerError) 
            
            if self.graph:
                DataVis.graphDataAll(training[polyType], pred, test[polyType], self.ticker, polyType, "FFT")
                #DataVis.graphDataResults(pred, test[polyType], self.ticker, polyType, "FFT")
    
            # Add Row
            table.add_row(["FFT", str(dev)[:7], str(perError)[:7], str(oneDev)[:7], str(onePerError)[:7],str(onePerError)[:7], str(lastDev)[:7], polyType.upper()])

        ### Print Table
        if self.table:
            DataVis.displayTable(table)
            
    def getData(self):
        return self.regType, self.dev, self.perError, self.oneDev, self.onePerError, self.lastDev, self.lastPerError, self.trainEndVal, self.testEndVal