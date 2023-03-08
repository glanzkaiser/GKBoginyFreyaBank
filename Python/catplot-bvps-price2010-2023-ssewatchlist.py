# https://towardsdev.com/multi-dimension-visualization-in-python-part-i-85c13e9b7495
# https://towardsdev.com/multi-dimension-visualization-in-python-part-ii-8c56d861923a
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns

datassebluechip = pd.read_csv("/home/browni/LasthrimProjection/Python/csv/ssewatchlistbluechipstocks.csv", index_col=0, parse_dates = True)

# Store stocks type as an attribute
datassebluechip['stocks_type'] = 'SSE Blue chip'

# bucket stocks quality scores into qualitative quality labels
datassebluechip['PER 2023'] = datassebluechip['per2023'].apply(lambda value: 'low'
		if value <= 10 
		else 'medium' if value <= 15
		else 'high')
datassebluechip['PER 2023'] = pd.Categorical(datassebluechip['PER 2023'],
			categories=['low','medium','high'])

# catplot BVPS and Price March 2023

allssestocksbluechip = pd.melt(datassebluechip, id_vars="company", value_vars=['bvps2023', 'pricejan2010', 'pricemar2023'])
print(datassebluechip)

bluechip_plot = sns.catplot(x='company', y='value', hue='variable', data=allssestocksbluechip, kind='bar')
plt.title('Bar Chart for SSE China Blue Chip Book Value March 2023 vs Price 2010-2023')
plt.xticks(rotation = 88) # Rotates X-Axis Ticks by 88-degrees
plt.show()

bluechip_plot.figure.savefig("ssebluechipoutput.png", dpi=400)
