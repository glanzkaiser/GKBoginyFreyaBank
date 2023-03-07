# https://towardsdev.com/multi-dimension-visualization-in-python-part-i-85c13e9b7495
# https://towardsdev.com/multi-dimension-visualization-in-python-part-ii-8c56d861923a
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns

dataidxbluechip = pd.read_csv("/home/browni/LasthrimProjection/Python/csv/idxwatchlistbluechipstocks.csv", index_col=0, parse_dates = True)
dataidxpenny = pd.read_csv("/home/browni/LasthrimProjection/Python/csv/idxwatchlistpennystocks.csv", index_col=0, parse_dates = True)

# Print first 5 rows of data
print(dataidxbluechip.head())
print(dataidxpenny.head())

# Store stocks type as an attribute
dataidxbluechip['stocks_type'] = 'IDX Blue chip'
dataidxpenny['stocks_type'] = 'IDX Penny Stocks'

# bucket stocks quality scores into qualitative quality labels
dataidxbluechip['PER 2023'] = dataidxbluechip['per2023'].apply(lambda value: 'low'
		if value <= 10 
		else 'medium' if value <= 15
		else 'high')
dataidxbluechip['PER 2023'] = pd.Categorical(dataidxbluechip['PER 2023'],
			categories=['low','medium','high'])

dataidxpenny['PER 2023'] = dataidxpenny['per2023'].apply(lambda value: 'low'
		if value <= 10 
		else 'medium' if value <= 15
		else 'high')
dataidxpenny['PER 2023'] = pd.Categorical(dataidxpenny['PER 2023'],
			categories=['low','medium','high'])

allstocks = pd.concat([dataidxbluechip, dataidxpenny])

# Print first 5 rows of data after being concatenate and replace
# the column of per2023 with PER 2023 stating the level of PER
print(allstocks.head())

# catplot BVPS and Price March 2023

allstocksbluechip = pd.melt(dataidxbluechip, id_vars="company", value_vars=['bvps2023', 'pricejan2010', 'pricemar2023'])
print(allstocksbluechip)

bluechip_plot = sns.catplot(x='company', y='value', hue='variable', data=allstocksbluechip, kind='bar')
plt.title('Bar Chart for Indonesian Blue Chip Book Value March 2023 vs Price 2010-2023')
plt.xticks(rotation = 88) # Rotates X-Axis Ticks by 88-degrees
plt.show()

bluechip_plot.figure.savefig("bluechipoutput.png", dpi=600)

allstockspenny = pd.melt(dataidxpenny, id_vars="company", value_vars=['bvps2023', 'pricejan2010', 'pricemar2023'])
print(allstockspenny)

penny_plot = sns.catplot(x='company', y='value', hue='variable', data=allstockspenny, kind='bar')
plt.title('Bar Chart for Indonesian Penny Stocks Book Value March 2023 vs Price 2010-2023')
plt.xticks(rotation = 88) # Rotates X-Axis Ticks by 88-degrees
plt.show()

penny_plot.figure.savefig("pennyoutput.png", dpi=600)
