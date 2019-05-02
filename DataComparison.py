'''
    Data Comparison Class (Average Deviation & Average Percent Error)
'''
class DataComparison:
    def averageDev(dataPred, dataTest):
        '''
            Calculate Average Deviation
        '''
        totalDev = 0
        
        for ii in range(0,len(dataTest)):
            totalDev += dataPred[ii]-dataTest[ii]
            
        return (totalDev / len(dataTest))
    
    def averagePerError(dataPred, dataTest):
        '''
            Calculate Average Percent Error
        '''
        totalErr = 0
        
        for ii in range(0,len(dataTest)):
            totalErr += (dataPred[ii]-dataTest[ii]) / dataTest[ii]
            
        #return abs((totalErr / len(dataTest)) * 100)
        return (totalErr / len(dataTest) * 100)
    
    def dayOneAccuracy(dataPred, dataTest):
        '''
            Calculate Accuracy of First Predicted Day
        '''
        dev = dataPred[0] - dataTest[0]
        #perErr = abs((dev / dataTest[0])) * 100
        perErr = (dev / dataTest[0]) * 100
        
        return dev, perErr
    
    def lastDayAccuracy(dataPred, dataTest):
        '''
            Calculate Accuracy of Last Predicted Day
        '''
        dev = dataPred[len(dataPred)-1] - dataTest[len(dataPred)-1]
        #perErr = abs((dev / dataTest[len(dataPred)-1])) * 100
        perErr = (dev / dataTest[len(dataPred)-1]) * 100
        
        return dev, perErr