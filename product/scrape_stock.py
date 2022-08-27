# Import yfinance and matplotlib
import yfinance as yf  
import matplotlib.pyplot as plt
# Get the data for the SPY ETF by specifying the stock ticker, start date, and end date
data = yf.download('SPY','2015-01-01','2020-01-01')
print(data)
# # Plot the close prices
# data["Adj Close"].plot()
# plt.show()