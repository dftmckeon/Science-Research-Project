'''
    Regressions Class
'''

import numpy as np
from numpy import fft

class Regressions:
    def __init__(self, data):
        # Separate Data Values
        day =  data[0]
        volume = data[1]
        dayOpen = data[2]  
        dayClose = data[3] 
        dayHigh = data[4] 
        dayLow = data[5]
                
    def polyReg(day, dayPrice):
        '''
            Polynomial Regression of Daily Prices
        '''        
        rSq = 0.0     # R-Squared
        degree = 0    # PolyReg Degree 
        
        x = np.array(day)
        y = np.array(dayPrice)
        
        while rSq < 0.9:
            # Increments Degree Until R^2 > 0.9
            degree += 1
            
            regVals = np.polyfit(x, y, degree)
            
            coeffs = regVals.tolist()
            f = np.poly1d(coeffs)
            
            yhat = f(x)
            ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
            
            ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
            sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
            
            rSq = ssreg / sstot
    
        return f.c 
                        
    def fastFourier(dayPrice, testSize):
        '''
            Fast Fourier Transform of Daily Prices
        '''
        dayPrice = np.array(dayPrice)
        n = dayPrice.size
        harm = 20                               # number of harmonics in model
        t = np.arange(0, n)
        p = np.polyfit(t, dayPrice, 1)          # find linear trend in x
        x_notrend = dayPrice - p[0] * t         # detrended x
        x_freqdom = fft.fft(x_notrend)          # detrended x in frequency domain
        f = fft.fftfreq(n)                      # frequencies
        indexes = list(range(n))
        
        # sort indexes by frequency, lower -> higher
        indexes.sort(key = lambda i: np.absolute(f[i]))
 
        t = np.arange(0, n + len(testSize))
        restored_sig = np.zeros(t.size)
        for i in indexes[:1 + harm * 2]:
            ampli = np.absolute(x_freqdom[i]) / n   # amplitude
            phase = np.angle(x_freqdom[i])          # phase
            restored_sig += ampli * np.cos(2 * np.pi * f[i] * t + phase)
            
        return restored_sig + p[0] * t