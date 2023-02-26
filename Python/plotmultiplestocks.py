from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()
y_symbols = ['EA', 'TTWO', 'ATVI']

from datetime import datetime
startdate = datetime(2000,1,1)
enddate = datetime(2023,1,31)
data = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)

#print(data)

#data['Close'].plot()


plt.figure(figsize=(20,10))
plt.plot(data.index, data['Close'])
plt.xlabel("Date")
plt.ylabel("Price (in USD)")
plt.title("Game Corporation Stock Price 1/1/00 - 1/1/23")
plt.show()