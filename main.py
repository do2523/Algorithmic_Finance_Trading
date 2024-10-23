import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import brute
import matplotlib.pyplot as plt
from datetime import datatime, timedelta

class VectorizedBacktester:
    '''
    Class for the vectorized backtesting of simple MA-based trading strategies.

    Attributes:
    Symbol: str
        ticker symbol with which to work with
    Start: str
        Start date for data import (YYYY-MM-DD)
    end: str
        End date for data import (YYYY-MM-DD)
    amount: float
        The amount to be invested at the beginning
    tc: float
        proportional transaction costs per trade (0.5% = 0.005)
    '''

    def __init__(self, symbol, start, end, amount, tc):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.amount = amount
        self.tc = tc
        self.results = None
        self.get_data()

    def get_data(self):
        '''imports the data from Yahoo Finance and creates a DataFrame with prices'''
        ticker = yf.ticker(self.symbol)
        raw = ticker.history(start=self.start, end=self.end, interval='1d')
        raw['returns'] = np.log(raw['Close'] / raw['Close'].shift(1))
        raw['price'] = raw['Close']
        self.data = raw
    
    def set_parameters(self, **kwargs):
        '''Set the parameters for the strategy'''

        for key in kwargs.keys():
            setattr(self, key, kwargs[key])
    
    def test_strategy(self):
        '''Backtests the trading strategy and calculates comprehensive metrics'''
        data = self.data.copy().dropna()
        data['position'] = self.generate_signals()
        data['strategy'] = data['position'].shift(1) * data['returns']
        data['trades'] = data.position.diff().fillna(0).abs()
        data['strategy'] = data['strategy'] - data['trades'] * self.tc
    
