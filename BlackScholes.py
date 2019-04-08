'''
   Black Scholes Class 
'''

import numpy as np
import scipy.stats as si

class BlackScholes:
    def __init__(self, args):   
        #S: spot price
        #K: strike price
        #r: interest rate
        #sigma: implied volatility
        #T: time to maturity
        #premium: price of option
        
        S = args[0]
        K = args[1]
        r = args[2]
        sigma = args[3]
        T = args[4]
        #premium = args[5]
        premium = self.callPremium(S, K, r, sigma, T)
        sigmaTheo = self.callIV(S, K, r, T, premium)
                
        print("Stock Price:\t\t", S)
        print("Strike Price:\t\t", K)
        print("Risk-free rate:\t\t", r)
        print("Implied Volatility:\t", sigma)
        print("Time to Maturity:\t", T)
        print("-\t\t\t-")
        print("Call Premium:\t\t", premium)
        print("Call IV:\t\t", sigmaTheo)
        
    def callPremium(self, S, K, r, sigma, T):
        #S: spot price
        #K: strike price
        #T: time to maturity
        #r: interest rate
        #sigma: implied volatility
        
        T = float(T)/365
        
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        
        premium = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
        
        return premium
        
    def callIV(self, S, K, r, T, premium):
        #S: spot price
        #K: strike price
        #T: time to maturity
        #r: interest rate
        #premium: price of option
        
        T = float(T)/365
        sigma = 0.0
        premiumTest = 0.0
        
        while abs(premiumTest - premium) > 0.1:
            sigma += 0.005
            
            d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
            d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
            
            premiumTest = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
            
        return str(sigma)[:6]