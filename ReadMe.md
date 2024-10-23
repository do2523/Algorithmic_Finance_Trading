# VectorizedBacktester

**Building a professional-grade trading backtester from scratch using Python.** Developed a powerful tool that connects to real-time market data, tests multiple trading strategies, and performs sophisticated performance analysis. Using Python libraries such as yfinance, numpy and pandas.

The **VectorizedBacktester** class simplifies backtesting by automating data downloads, return calculations, and the evaluation of trading strategies.

## Key Attributes:
- **Symbol**: The stock or asset being traded (e.g., AAPL for Apple stock).
- **Start and End**: The date range for the historical data.
- **Amount**: Initial capital invested.
- **TC**: Transaction costs, representing commissions or slippage in real-world trading.

The class uses the `yfinance` package to fetch historical price data, calculates daily log returns, and applies the chosen trading strategy.

## Trading Strategies:

### Moving Average (MA)
This strategy compares two Simple Moving Averages (SMAs):
- **SMA1**: Short-term moving average (e.g., 50 days).
- **SMA2**: Long-term moving average (e.g., 200 days).

A buy signal is generated when the short-term average crosses above the long-term average, and a sell signal occurs when it crosses below.

### Relative Strength Index (RSI)
RSI measures price momentum to identify overbought or oversold conditions:
- **Upper bound**: Overbought signal (e.g., RSI > 70).
- **Lower bound**: Oversold signal (e.g., RSI < 30).

Buy and sell decisions are based on crossing these thresholds.

## Strategy Metrics:

- **Total Return**:  
  `Total Return = (Final Value - Initial Value) / Initial Value`  
  Shows the overall performance of the strategy.

- **Excess Return**:  
  The difference between the total return and the market return.

- **Volatility**:  
  Measures the risk by showing how much the returns fluctuate.

- **Sharpe Ratio**:  
  `Sharpe Ratio = (Average Return - Risk-Free Rate) / Volatility`  
  This metric adjusts returns by risk, measuring the reward per unit of risk. A higher Sharpe ratio indicates better risk-adjusted returns.
