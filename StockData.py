import csv

class StockData:        
    def __init__(self, csvFile, startDate, duration):
        '''
        '''        
        self.day = []         # Day Number
        self.volume = []      # Trading Volume
        self.start = []       # Opening Price
        self.close = []       # Closing Price
        self.high = []        # Highest Price
        self.low = []         # Lowest Price
        self.adjust = []      # Adjust Close Price
        
        with open("TickerData/" + csvFile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0       
            endDate = startDate + duration
            for row in csv_reader:
                line += 1
                if line >= startDate and line < endDate:
                    dayNum = line-startDate+1
                    self.day.append(float(dayNum))
                    self.volume.append(float(row[1]))
                    self.start.append(float(row[2]))
                    self.close.append(float(row[3]))
                    self.high.append(float(row[4]))
                    self.low.append(float(row[5]))
                    self.adjust.append(float(row[6]))
                    
        self.data = {
            "day"     : self.day,
            "volume"  : self.volume,
            "start"   : self.start,
            "close"   : self.close,
            "high"    : self.high,
            "low"     : self.low,
            "adjust"  : self.adjust,
        }