import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

company = 'ATVI'

# Define a start date and End Date
start = dt.datetime(2000,1,1)
end =  dt.datetime(2023,1,1)

# Read Stock Price Data 
data = yf.download(company, start , end)

#data.tail(10)
#print(data)

# Creating and Plotting Moving Averages
data["SMA1"] = data['Close'].rolling(window=50).mean()
data["SMA2"] = data['Close'].rolling(window=200).mean()
data['ewma'] = data['Close'].ewm(halflife=0.5, min_periods=20).mean()

plt.figure(figsize=(10,10))
plt.plot(data['SMA1'], 'g--', label="SMA1")
plt.plot(data['SMA2'], 'r--', label="SMA2")
plt.plot(data['Close'], label="Close")
plt.title("Activision Blizzard Stock Price 1/1/00 - 1/1/23")
plt.legend()
plt.show()