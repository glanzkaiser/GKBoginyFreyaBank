# https://towardsdev.com/multi-dimension-visualization-in-python-part-i-85c13e9b7495
# https://towardsdev.com/multi-dimension-visualization-in-python-part-ii-8c56d861923a
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns

dataidxbluechip = pd.read_csv("/home/browni/LasthrimProjection/Python/csv/idxbluechipstocks.csv", index_col=0, parse_dates = True)
dataidxpenny = pd.read_csv("/home/browni/LasthrimProjection/Python/csv/idxpennystocks.csv", index_col=0, parse_dates = True)

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

# Visualizing 5-D mix data using bubble charts
# leveraging the concepts of hue, size and depth

g = sns.FacetGrid(allstocks, col="stocks_type", hue='PER 2023',
                  col_order=['IDX Blue chip', 'IDX Penny Stocks'], 
	 	  hue_order=['low', 'medium', 'high'],
                  aspect=1.2, palette=sns.light_palette('navy', 4)[1:])

# The size='bvps2023' seems problematic.. ask..
g.map_dataframe(sns.scatterplot, "pricejan2010", "debtequityratio2023", alpha=0.9, 
      edgecolor='white', linewidth=0.5, size='revenue2021', 
      sizes=(33, 230))
# sizes=(allstocks['bvps2023'].min(), allstocks['bvps2023'].max()) will create huge dots
# thus I changed it into sizes=(10,230)
fig = g.fig 
fig.subplots_adjust(top=0.8, wspace=0.3)
fig.suptitle('Stocks 5D Scatter Plot with Revenue 2021(the bubble size)', fontsize=14)
l = g.add_legend(title='Stocks PER Level')

plt.show()
fig.savefig('5dscatterplot.png')