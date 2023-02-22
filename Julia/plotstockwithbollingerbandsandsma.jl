using CSV, Dates, DataFrames, Plots, Plots.PlotMeasures, RollingFunctions

fileindy = "./csv/IDX-Stocks/INDY Historical Data.csv"

dfindy = CSV.read(fileindy, DataFrame)

dfindy.Price .= parse.(Float64, replace.(dfindy.Price, "," => ""))
dfindy[!,"Change %"] .= parse.(Float64, replace.(dfindy[!,"Change %"], "%" => ""))

dfindy.Dates = Date.(dfindy.Date, "mm/dd/yyyy")
tick_years = Date.(unique(Dates.year.(dfindy.Dates)))
DateTick = Dates.format.(tick_years, "yy")
xlimsindy = extrema([tick_years; dfindy.Dates])

p1 = plot(dfindy.Dates, dfindy.Price, title="",
    xticks=(tick_years,DateTick), xlims=xlimsindy,
    label="Indika Energy (Price)", xlabel="", ylabel="")

# Set up MA and Bollinger Band
prices = dfindy.Price;
moving_average = rollmean(prices, 20);
moving_std = rollstd(prices, 20);

bollinger_high = moving_average .+ 2moving_std;
bollinger_low = moving_average .- 2moving_std;

p2 = plot([moving_average bollinger_low bollinger_high], 
	label = ["Moving average" "Low" "High"], ls = [:solid :dash :dash])

plot(p1, p2, size=(900,800), layout = (2, 1), 
    legend=:outerright, left_margin=10mm, bottom_margin=5mm,
     xaxis = "", yaxis = "")
