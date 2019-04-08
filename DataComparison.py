'''
    Data Comparison Class (Average Deviation & Average Percent Error)
'''
class DataComparison:
    def __init__(self, dataPred, dataTest):
        '''
            Main
        ''' 
        
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
            
        return abs((totalErr / len(dataTest)) * 100)