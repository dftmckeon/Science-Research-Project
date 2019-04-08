'''
    Predictive Modeling for Options/Standard Trading
    10/2/2018
    Daniel McKeon
---
    Current Test Ideas
        - Machine Learning (Pattern Analysis)
        - Probability/Risk Analysis
        - Sentiment Analysis
        - Black Scholes Derivations
        - LSTM
        - Distance of IV from HV
    Implemented Tests
        - Polynomial Regression
        - FFT
    Current Tickers
        - SBUX
        - AAPL
        - TSLA
'''
import numpy as np
import csv
from prettytable import PrettyTable

from Regressions import Regressions as Reg
from DataComparison import DataComparison as DataComp

class Analysis():    
    def __init__(self):
        '''
            Handles Tickers & Runs algorithm()
        '''
        # Company Tickers
        tickerList = ("SBUX", "AAPL", "TSLA")
    
        for ticker in tickerList:   
            print()
            
            sepLine = ""
            for ii in range(0,len(ticker)+6):
                sepLine += "#"
                
            print(sepLine)
            print("## "+ticker+" ##")
            print(sepLine)
            
            csv = ticker+".csv"
            self.algorithm(csv)
        
    def algorithm(self, csv):
        '''
            Main Outline:
                
            - Import Values
                - Training
                - Test
                
            - PolyReg (Low)
            - PolyReg (Closing)
            - FFT (Closing)
            - FFT (High)
            - FFT (Low)
        '''
        #######################
        ### Data Extraction ###
        #######################
        
        # Training Data (3 Months)
        dataTraining = self.dataExtractTraining(csv)
        dayTraining = dataTraining[0]
        volumeTraining = dataTraining[1]
        dayOpenTraining = dataTraining[2]  
        dayCloseTraining = dataTraining[3] 
        dayHighTraining = dataTraining[4] 
        dayLowTraining = dataTraining[5]
        dayAdjCloseTraining = dataTraining[6]
        
        # Testing Data (1 Month)
        dataTest = self.dataExtractTest(csv, dataTraining[7])
        dayTest = dataTest[0]
        volumeTest = dataTest[1]
        dayOpenTest = dataTest[2]  
        dayCloseTest = dataTest[3] 
        dayHighTest = dataTest[4] 
        dayLowTest = dataTest[5]  
        dayAdjCloseTest = dataTest[6]
        
        # Table
        table = PrettyTable()
        table.field_names = ["Method", "Avg. Dev.", "Per. Error", "Price"]
        
        
        ####################################################
        ### Polynomial Regression w/ Lowest Daily Prices ###
        ####################################################
        
        # Regressions
        coeffs = Reg.polyReg(dayTraining, dayLowTraining)
        f = np.poly1d(coeffs)
        
        # Predicted Prices
        pred = f(dayTest)
        
        # Average Deviation & Average Percent Error of Predicted Test Prices
        dev = DataComp.averageDev(pred, dayLowTest)
        perError = DataComp.averagePerError(pred, dayLowTest)

        # Add Row
        table.add_row(["Poly Reg", str(dev), str(perError), "Low"])


        #####################################################
        ### Polynomial Regression w/ Daily Closing Prices ###
        #####################################################
        
        # Regressions
        coeffs = Reg.polyReg(dayTraining, dayCloseTraining)
        f = np.poly1d(coeffs)
        
        # Predicted Prices
        pred = f(dayTest)
        
        # Average Deviation & Average Percent Error of Predicted Test Prices
        dev = DataComp.averageDev(pred, dayCloseTest)
        perError = DataComp.averagePerError(pred, dayCloseTest)

        # Add Row
        table.add_row(["Poly Reg", str(dev), str(perError), "Close"])

        #######
        ###     FFFFF
        ###     F
        ###     FFF
        ###     F
        ###     F
        #######

        #####################################################################
        ### Fast Fourier Transform w/ Daily Opening Prices (20 Harmonics) ###
        #####################################################################         
        # Regressions & Predicted Prices
        pred = Reg.fastFourier(dayOpenTraining, dayTest)
        
        # Average Deviation & Average Percent Error of Predicted Test Prices
        dev = DataComp.averageDev(pred, dayOpenTest)
        perError = DataComp.averagePerError(pred, dayOpenTest)

        # Add Row
        table.add_row(["FFT", str(dev), str(perError), "Open"])


        #####################################################################
        ### Fast Fourier Transform w/ Daily Closing Prices (20 Harmonics) ###
        #####################################################################               
        # Regressions & Predicted Prices
        pred = Reg.fastFourier(dayCloseTraining, dayTest)
        
        # Average Deviation & Average Percent Error of Predicted Test Prices
        dev = DataComp.averageDev(pred, dayCloseTest)
        perError = DataComp.averagePerError(pred, dayCloseTest)

        # Add Row
        table.add_row(["FFT", str(dev), str(perError), "Close"])


        ###################################################################
        ### Fast Fourier Transform w/ Daily High Prices (20 Harmonics)  ###
        ###################################################################       
        # Regressions & Predicted Prices
        pred = Reg.fastFourier(dayHighTraining, dayTest)
        
        # Average Deviation & Average Percent Error of Predicted Test Prices
        dev = DataComp.averageDev(pred, dayHighTest)
        perError = DataComp.averagePerError(pred, dayHighTest)

        # Add Row
        table.add_row(["FFT", str(dev), str(perError), "High"])


        ################################################################# 
        ### Fast Fourier Transform w/ Daily Low Prices (20 Harmonics) ###
        #################################################################
        # Regressions & Predicted Prices
        pred = Reg.fastFourier(dayLowTraining, dayTest)
        
        # Average Deviation & Average Percent Error of Predicted Test Prices
        dev = DataComp.averageDev(pred, dayLowTest)
        perError = DataComp.averagePerError(pred, dayLowTest)
        
        # Add Row
        table.add_row(["FFT", str(dev), str(perError), "Low"])
                
        ### Print Table
        print()
        print(table)
        
    def dataExtract(self, csvFile):
        '''
            Extracts data from CSV
        '''
        day = []        # Day Number
        volume = []     # Trading Volume
        dayOpen = []    # Opening Price
        dayClose = []   # Closing Price
        dayHigh = []    # Highest Price
        dayLow = []     # Lowest Price
        
        with open(csvFile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in csv_reader:
                if line == 0:
                    line += 1
                else:
                    day.append(float(row[0]))
                    volume.append(float(row[1]))
                    dayOpen.append(float(row[2]))
                    dayClose.append(float(row[3]))
                    dayHigh.append(float(row[4]))
                    dayLow.append(float(row[5]))
                    
        return day, volume, dayOpen, dayClose, dayHigh, dayLow
        
    def dataExtractTraining(self, csvFile):
        '''
            Extracts training data from CSV (3 Months)
        '''
        day = []        # Day Number
        volume = []     # Trading Volume
        dayOpen = []    # Opening Price
        dayClose = []   # Closing Price
        dayHigh = []    # Highest Price
        dayLow = []     # Lowest Price
        dayAdjClose = []# Adjust Close Price
        
        with open(csvFile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0       
            startDate = 200
            endDate = startDate + 90
            for row in csv_reader:
                line += 1
                if line >= startDate and line < endDate:
                    dayNum = line-startDate+1
                    day.append(float(dayNum))
                    volume.append(float(row[1]))
                    dayOpen.append(float(row[2]))
                    dayClose.append(float(row[3]))
                    dayHigh.append(float(row[4]))
                    dayLow.append(float(row[5]))
                    dayAdjClose.append(float(row[6]))
                    
        return day, volume, dayOpen, dayClose, dayHigh, dayLow, dayAdjClose, endDate
    
    def dataExtractTest(self, csvFile, startDate):
        '''
            Extracts test data from CSV (1 Month)
        '''
        day = []        # Day Number
        volume = []     # Trading Volume
        dayOpen = []    # Opening Price
        dayClose = []   # Closing Price
        dayHigh = []    # Highest Price
        dayLow = []     # Lowest Price
        dayAdjClose = []# Adjust Close Price
        
        with open(csvFile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0   
            endDate = startDate + 30
            for row in csv_reader:
                line += 1
                if line >= startDate and line < endDate:
                    dayNum = line-startDate+1
                    day.append(float(dayNum))
                    volume.append(float(row[1]))
                    dayOpen.append(float(row[2]))
                    dayClose.append(float(row[3]))
                    dayHigh.append(float(row[4]))
                    dayLow.append(float(row[5]))      
                    dayAdjClose.append(float(row[6]))
        
        return day, volume, dayOpen, dayClose, dayHigh, dayLow, dayAdjClose
                    
# Run Program
Analysis()                 