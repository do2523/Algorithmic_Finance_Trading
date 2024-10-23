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