using CSV, DataFrames, Plots, Plots.PlotMeasures

file = "./csv/Shanghai Composite Historical Data.csv"
filedj = "./csv/Dow Jones Industrial Average Historical Data.csv"
filenasdaq = "./csv/NASDAQ Composite Historical Data.csv"
filenikkei = "./csv/Nikkei 225 Historical Data.csv"

df = CSV.read(file, DataFrame)
df2 = CSV.read(filedj, DataFrame)
df3 = CSV.read(filenasdaq, DataFrame)
df4 = CSV.read(filenikkei, DataFrame)

df[!,"Change %"] .= parse.(Float64, replace.(df[!,"Change %"], "%" => ""))
df2[!,"Change %"] .= parse.(Float64, replace.(df2[!,"Change %"], "%" => ""))
df3[!,"Change %"] .= parse.(Float64, replace.(df3[!,"Change %"], "%" => ""))
df4[!,"Change %"] .= parse.(Float64, replace.(df4[!,"Change %"], "%" => ""))

p1 = histogram(df[!,"Change %"], title="",
	label="Shanghai Composite Index (SSE)", xlabel="", ylabel="")
p2 = histogram(df2[!,"Change %"], title="",
	label="Dow Jones Industrial Average", xlabel="", ylabel="")
p3 = histogram(df3[!,"Change %"], title="",
	label="NASDAQ", xlabel="", ylabel="")
p4 = histogram(df4[!,"Change %"], title="",
	label="Nikkei 225", xlabel="", ylabel="")

plot(p1, p2, p3, p4, size=(1200,800), layout = (4, 1), 
	legend=:outerright, left_margin=10mm, bottom_margin=5mm,
     xaxis = "Change (in %)", yaxis = "Frequencies")