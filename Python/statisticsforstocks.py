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
# re-shuffle records just to randomize data points
allstocks = allstocks.sample(frac=1, random_state=42).reset_index(drop=True)

# Print first 5 rows of data after being concatenate and replace
# the column of per2023 with PER 2023 stating the level of PER
print(allstocks.head())

#
# Correlation Matrix Heatmap
f, ax = plt.subplots(figsize=(10, 6))
corr = allstocks.corr()
hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f',
                 linewidths=.05)
f.subplots_adjust(top=0.93)
t= f.suptitle('Stocks Correlation Heatmap', fontsize=14)

plt.show()
f.savefig('correlationchart.png')

# Multi-bar Plot
cp = sns.countplot(x="per2023", hue="stocks_type", data=allstocks, 
                   palette={"IDX Blue chip": "#FF9999",  "IDX Penny Stocks": "#FFE888"})
plt.title('Bar Chart for Stocks')
plt.show()

figureseaborn = cp.get_figure()    
figureseaborn.savefig('barchart.png', dpi=400)

# Box Plots
f, (ax) = plt.subplots(1, 1, figsize=(12, 4))
f.suptitle('IDX Stocks PER Quality - Debt Equity Ratio', fontsize=14)

sns.boxplot(x="per2023", y="debtequityratio2023", data=allstocks,  ax=ax)
ax.set_xlabel("Price Earning Ratio 2023",size = 12,alpha=0.8)
ax.set_ylabel("Debt Equity Ratio (%)",size = 12,alpha=0.8)

plt.show()
f.savefig('boxplot.png')

# Visualizing 3-D numeric data with Scatter Plots
# length, breadth and depth
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

xs = allstocks['pricejan2010']
ys = allstocks['bvps2023']
zs = allstocks['per2023']
ax.scatter(xs, ys, zs, s=50, alpha=0.6, edgecolors='w')

ax.set_xlabel('Price in January 2010 / at IPO')
ax.set_ylabel('Book Value in 2023')
ax.set_zlabel('Price Earning Ratio in 2023')

plt.title('3D Plot for Price, Book Value and PER')
plt.show()
fig.savefig('3dplot.png')

# Visualizing 4-D mix data using scatter plots
# leveraging the concepts of hue and depth
fig = plt.figure(figsize=(8, 6))
t = fig.suptitle('4D Plot for Price, Book Value and PER', fontsize=14)
ax = fig.add_subplot(111, projection='3d')

xs = list(allstocks['pricejan2010'])
ys = list(allstocks['bvps2023'])
zs = list(allstocks['per2023'])
data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]
colors = ['blue' if wt == 'IDX Blue chip' else 'orange' for wt in list(allstocks['stocks_type'])]

for data, color in zip(data_points, colors):
    x, y, z = data
    ax.scatter(x, y, z, alpha=0.4, c=color, edgecolors='none', s=30)

ax.set_xlabel('Price in January 2010 / at IPO')
ax.set_ylabel('Book Value per Share 2023')
ax.set_zlabel('Price Earning Ratio 2023') 

plt.show()
fig.savefig('4dplot.png')

# Visualizing 4-D mix data using scatter plots
# leveraging the concepts of hue and facets for > 1 categorical attributes

g = sns.FacetGrid(allstocks, col="stocks_type", hue='PER 2023',
                  col_order=['IDX Blue chip', 'IDX Penny Stocks'], 
	 	  hue_order=['low', 'medium', 'high'],
                  aspect=1.2, palette=sns.light_palette('navy', 4)[1:])

g.map(plt.scatter, "pricejan2010", "debtequityratio2023", alpha=0.9, 
      edgecolor='white', linewidth=0.5, s=100)

fig = g.fig 
fig.subplots_adjust(top=0.8, wspace=0.3)
fig.suptitle('4D Stocks Type - Book Value - Debt Equity Ratio - PER 2023', fontsize=14)
l = g.add_legend(title='Stocks PER Quality Class')

plt.show()
fig.savefig('4dscatterplot.png')
