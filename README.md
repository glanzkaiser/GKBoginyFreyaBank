# GKBoginyFreyaBank

```
Meski waktu datang dan berlalu sampai kau tiada bertahan
Semua takkan mampu mengubahku
Hanyalah kau yang ada di relungku
Hanyalah dirimu mampu membuatku jatuh dan mencinta
Kau bukan hanya sekedar indah
Kau takkan terganti

- From Glanz to Freya (Kahitna - Takkan Terganti song)
- From Freya to Glanz (I make you listen to it first -Freya)
```

A place to put codes that can help us to make decision on which to invest, where to invest. If I have USD 10,000 now and want to make USD 100,000 under 1 year perhaps stocks market is the best place, but which one? Since bonds is safe but the yield is not as high as stocks. 

#### In March 2019, GGRM from IDX / JKSE falls from IDR 90,000 to IDR 17,000 in January 2023. Is IDR 17,000 still overprice? We can see that the highest price is IDR 90,000. When will it hit the bottom? Will it fall again? Check the annual report and calculate the margin of safety, the book value. Use the Jupyter Notebook here to help you if you want it, or just use your intuition.

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

# Ideas

1. Create C++ codes (scrape, or read from csv then plot) that can give same output like this Jupyter Notebook, but with higher performance.

# Sources

1. Julia Discourse

2. StackOverFlow

3. Graham, Benjamin. The Intelligent Investor 4th Edition

4. investing.com

5. Yahoo Finance
