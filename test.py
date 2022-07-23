from openbb_terminal import api as openbb
import matplotlib.pyplot as plt 

print("START")

aapl_data = openbb.stocks.load(
    ticker="aapl",
)
aapl_data = openbb.stocks.process_candle(aapl_data)


openbb.stocks.candle("AAPL", aapl_data, True)


# # Load stock data
# ticker = "AAPL"
# stock_data = openbb.stocks.load(ticker="aapl")

# # Create a matplotlib figure
# fig, axes = plt.subplots(3, 1, figsize=(10, 7))

# # Use GST to add charts to the axes of the created figure
# openbb.stocks.ta.macd(s_ticker=ticker, series=aapl["Close"], external_axes=axes[0:2])
# openbb.stocks.options.voi_yf(
#     ticker=ticker,
#     expiry="2022-03-11",
#     min_sp=110,
#     max_sp=210,
#     min_vol=0.3,
#     external_axes=[axes[2]],
# )

# # Show the figure with charts
# fig.show()


print("END")
