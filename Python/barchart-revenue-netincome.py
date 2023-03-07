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

# Barchart
cp = sns.barplot(x="company", y="revenue2021", hue="stocks_type", data=allstocks, 
                   palette={"IDX Blue chip": "#FF9999",  "IDX Penny Stocks": "#FFE888"})
plt.title('Bar Chart for Indonesian Stocks Revenue in 2021')
plt.xticks(rotation = 88) # Rotates X-Axis Ticks by 45-degrees
plt.show()

figureseaborn = cp.get_figure()    
figureseaborn.savefig('barchartrevenue.png', dpi=400)

# Barchart Net Income
cp = sns.barplot(x="company", y="netincome2021", hue="stocks_type", data=allstocks, 
                   palette={"IDX Blue chip": "#FF9999",  "IDX Penny Stocks": "#FFE888"})
plt.title('Bar Chart for Indonesian Stocks Net Income in 2021')
plt.xticks(rotation = 88) # Rotates X-Axis Ticks by 88-degrees
plt.show()

figureseaborn = cp.get_figure()    
figureseaborn.savefig('barchartnetincome.png', dpi=400)
