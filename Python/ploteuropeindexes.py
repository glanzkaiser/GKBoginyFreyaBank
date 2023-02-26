import yfinance as yf
import matplotlib.pyplot as plt

from pandas_datareader import data as pdr
from forex_python.converter import CurrencyRates
from datetime import datetime

cr = CurrencyRates()

# Get exchange rate between GBP and USD and EUR and USD
gbp_to_usd = cr.get_rate('GBP', 'USD')
eur_to_usd = cr.get_rate('EUR', 'USD')

yf.pdr_override()
y_symbols = ['^FTSE', '^GDAXI', '^FCHI', '^STOXX50E','^N100', '^BFX']
startdate = datetime(2000,1,1)
enddate = datetime(2023,1,31)
data = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)

data.rename(columns={'^FTSE': 'FTSE 100 Index', 
                     '^GDAXI': 'DAX Index', 
                     '^FCHI': 'CAC 40 Index', 
                     '^STOXX50E': 'EURO STOXX 50 Index',
                     '^N100': 'Euronext 100 Index', 
                     '^BFX': 'BEL 20 Index'}, inplace=True)

plt.figure(figsize=(20,10))
plt.plot(data.index, data['Close'], label=data["Close"].columns)

plt.xlabel("Date")
plt.ylabel("Price (in its own currency)")
plt.title("Europe Indexes 1/1/00 - 1/1/23")
plt.legend()
plt.show()