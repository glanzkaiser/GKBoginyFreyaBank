using CSV, DataFrames, Plots, Plots.PlotMeasures

filejak = "./csv/Jakarta Stock Exchange Composite Index Historical Data.csv"

dfjak = CSV.read(filejak, DataFrame)

dfjak.Price .= parse.(Float64, replace.(dfjak.Price, "," => ""))
dfjak[!,"Change %"] .= parse.(Float64, replace.(dfjak[!,"Change %"], "%" => ""))

p1 = histogram(dfjak.Price, title="",
	label="Jakarta Stock Exchange (Price)", xlabel="", ylabel="")
p2 = histogram(dfjak[!,"Change %"], title="",
	label="Jakarta Stock Exchange (% Change)", xlabel="", ylabel="")

plot(p1, p2, size=(1200,800), layout = (2, 1), 
	legend=:outerright, left_margin=10mm, bottom_margin=5mm,
     	xaxis = "", yaxis = "Frequencies")
