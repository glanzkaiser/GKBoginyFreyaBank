# GKBoginyFreyaBank

# Westces Briga Gamma Annual Report

We have established a corporation focusing on investing in stocks with name Westces Briga Gamma.

Learning from Warren Buffett who wrote Annual letter to Berkshire' shareholders, this is our own style to write and re-read again so we can learn from our past investment actions, to make more money in the future from stocks and bond markets.

Read more here:
<a href="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/Westces%20Briga%20Gamma%202024.pdf">WBG 2024</a>

GK Boginy Freya Bank Source of learning:
<a href="https://drive.google.com/drive/folders/1L2bVIraPKOpq2qvg4KQ43UmOvN_iPh7O?usp=sharing">Click here</a>


```
Meski waktu datang dan berlalu sampai kau tiada bertahan
Semua takkan mampu mengubahku
Hanyalah kau yang ada di relungku
Hanyalah dirimu mampu membuatku jatuh dan mencinta
Kau bukan hanya sekedar indah
Kau takkan terganti

- From Glanz to Freya (Kahitna - Takkan Terganti song)
- From Freya to Glanz (I make you listen to it first -Freya)


I wanna call the stars. Down from the sky. 
I wanna live a day. That never dies. 
I wanna change the world. Only for you. 
All the impossible. I wanna do

- From Glanz to Freya (When You Tell Me That You Love Me -Diana Ross)
```

A place to put codes that can help us to make decision on which to invest, where to invest. If I have USD 10,000 now and want to make USD 100,000 under 1 year perhaps stocks market is the best place, but which one? Since bonds is safe but the yield is not as high as stocks. 

#### From March 2019, GGRM listed in IDX / JKSE falls from IDR 90,000 to IDR 17,000 in January 2023. Is IDR 17,000 still overprice? We can see that the highest price is IDR 90,000. When will it hit the bottom? Will it fall again? Check the annual report and calculate the margin of safety, the book value. Based on the book "The Intelligent Investor" the price of IDR 90,000 in 2019 that is 4 times higher than GGRM book value per share gives too much promise, as it comes down to IDR 17,000 at the end of 2022 and at the beginning of 2023. To help you with computing, use the Jupyter Notebook here to help you if you want it, or just use your intuition.

# How to Setup

We have provided Jupyter Notebook along with its pdf as well for:

1. Julia Kernel version 1.7.3
2. Python Kernel version 3.9.13

Follow these steps:

1. Create an empty folder name it `GKBoginyFreyaBank`

2. Open terminal at the directory `GKBoginyFreyaBank` and type

```
julia --project="."

julia> using IJulia
julia> notebook()

(if you need to add packages:)
julia> ]

(GKBoginyFreyaBank) pkg> add DataFrames CSV Dates
```

3. Create a new notebook with Julia or Python3 kernel (why open it with Julia? Old habit die hard... I still use it for Lasthrim Projection writing anyway. Python that I use is from Conda inside Julia, so Julia is like the root here. While Python is the branch of the tree.)

4. You can copy the notebook I uploaded here. It is for 2023 GKBoginyFreya Bank report. Will be updated for each Python and Julia version, when I learn new methods or have new ideas from a lot of sources.

| Julia Notebook | Python Notebook |
| ------------- | ------------- | 
| <img src="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/GGRMchart.png" width="83%"> | <img src="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/USCanadaindexes.png" width="83%"> | 
| <a href="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/2023/GKBoginyFreyaBank-Julia.ipynb">Julia</a> | <a href="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/2023/GKBoginyFreyaBank-Python.ipynb">Python</a>  |

# Example: Julia Code

This is a code that can be run in Julia REPL through terminal, without Jupyter Notebook:

You need to download the BVIC historical data from investing.com, it is a monthly data, with date ascending from top is the oldest date.

```
using CSV, Dates, DataFrames, Plots, Plots.PlotMeasures, RollingFunctions

filebvic = "./csv/IDX-Stocks/BVIC Historical Data.csv"

dfbvic = CSV.read(filebvic, DataFrame)

dfbvic[!,"Change %"] .= parse.(Float64, replace.(dfbvic[!,"Change %"], "%" => ""))

dfbvic.Dates = Date.(dfbvic.Date, "mm/dd/yyyy")
tick_years = Date.(unique(Dates.year.(dfbvic.Dates)))
DateTick = Dates.format.(tick_years, "yy")
xlimsbvic = extrema([tick_years; dfbvic.Dates])

plot(dfbvic.Dates, dfbvic.Price, title="",
    xticks=(tick_years,DateTick), xlims=xlimsbvic,
    label="Bank Victoria (Price)", xlabel="", ylabel="")

# Set Book Value per Share
x = [Date("01/12/2018", "d/m/y"), Date("01/12/2019", "d/m/y"), Date("01/12/2020", "d/m/y"), Date("01/12/2021", "d/m/y")];
y = [267, 284, 252, 318];
plot!(x,y, label="Book Value per Share")
```

![Julia](https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/BVIC%20book%20value.png)

# Example: Python Code Statistics Full

This code can be run when opening terminal at the directory containing the python file (.py).

You can just type at terminal (assuming you are using python 3):

```
python3 statisticsforstocks.py
```

| Stocks Correlation Heatmap | 5D Scatter Plot Book Value and DER |
| ------------- | ------------- | 
| <img src="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/correlationchart.png" width="83%"> | <img src="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/5dscatterplot.png" width="83%"> | 
| <a href="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/Python/statisticsforstocks.py">statisticsforstocks</a> | <a href="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/Python/statisticsforstocks.py">statisticsforstocks</a>  |


Another example that you can type or just access here <a href="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/Python/catplot-bvps-price2010-2023.py">catplot</a> 
```
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

```

| Blue Chip | Penny Stocks |
| ------------- | ------------- | 
| <img src="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/bluechipoutput.png" width="83%"> | <img src="https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/pennyoutput.png" width="83%"> | 


# Nemiel

A PHP based code to scrape IDX stocks from Indopremier and show them in bootstrap sortable table, it can be run on localhost.

Perhaps it can't be used anymore since Indopremier might have changed their own security and codes. But, it still can be used to learn.

![Freya](https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/pdf.png)

![Freya](https://github.com/glanzkaiser/GKBoginyFreyaBank/blob/main/images/Nemiel1.png)

```
Nemiel is a nickname for Luc from Suikoden III, who is my best friend, and I am the Silmeria if Sasarai is Alicia.
 
That's complicated to ordinary person, but explains that it is connected between their realms and ours.

I will have a wonderful happiest marriage life with love like Luc and Sarah, Shiva and Parvati, and beyond..
-Glanz

```
# Ideas

1. Create C++ codes (scrape, or read from csv then plot) that can give same output like this Jupyter Notebook, but with higher performance.

# Push Update from Local / Computer to Github

```
git add .
git commit -m "I Love my Wife and I use GFreya OS"
git branch -M main
git remote add origin https://github.com/glanzkaiser/GKBoginyFreyaBank.git
git push -u origin main
```

# Sources

1. Julia Discourse

2. StackOverFlow

3. Graham, Benjamin. The Intelligent Investor 4th Edition

4. investing.com

5. Yahoo Finance
