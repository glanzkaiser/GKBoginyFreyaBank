import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

company = 'ATVI'

# Define a start date and End Date
start = dt.datetime(2017,1,1)
end =  dt.datetime(2023,1,1)

# Read Stock Price Data 
data = yf.download(company, start , end)

data = pd.read_csv("mydata.csv", index_col=0, parse_dates = True)

#data.tail(10)
#print(data)

# Creating and Plotting Bollinger Bands
data['middle_band'] = data['Close'].rolling(window=20).mean()
data['upper_band'] = data['Close'].rolling(window=20).mean() + data['Close'].rolling(window=20).std()*2
data['lower_band'] = data['Close'].rolling(window=20).mean() - data['Close'].rolling(window=20).std()*2

plt.figure(figsize=(10,10))
plt.plot(data['upper_band'], 'g--', label="upper")
plt.plot(data['middle_band'], 'r--', label="middle")
plt.plot(data['lower_band'], 'y--', label="lower")
plt.plot(data['Close'], label="Close")
plt.title("Activision Blizzard Stock Price 1/1/17 - 1/1/23")
plt.legend()
plt.show()