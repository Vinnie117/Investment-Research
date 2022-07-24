from openbb_terminal import api as openbb
import matplotlib.pyplot as plt 
import matplotlib
import matplotlib.rcsetup as rcsetup
from datetime import datetime
import pandas as pd

# https://stackoverflow.com/questions/7534453/matplotlib-does-not-show-my-drawings-although-i-call-pyplot-show
print(matplotlib.matplotlib_fname())
print(rcsetup.all_backends)
#matplotlib.rcParams['interactive'] == True

# https://stackoverflow.com/questions/21835847/matplotlib-show-method-does-not-open-window
# returns 'agg' -> non-interactive backend -> can only write to files!!
print(plt.get_backend())
matplotlib.use('Agg')

# To save plots using the non-interactive backends, use the matplotlib.pyplot.savefig('filename') method.
#####################################################################################
print("START")

aapl_data = openbb.stocks.load(ticker="aapl", start=datetime.strptime("2021-06-10", '%Y-%m-%d'))

# The data is in here
print(type(aapl_data))
print(aapl_data)
print(aapl_data.dtypes)
print(aapl_data.index.dtype)

# Euro conversion
usdeur = openbb.forex.load(to_symbol="EUR", from_symbol="USD", resolution='d', interval='1day', start_date="2021-06-10")
usdeur_close = usdeur['Close']
print(usdeur_close)

# Convert stock price to euro -> there are some dates missing (weekends)
aapl_data_eur = aapl_data['Close'] * usdeur_close
print(aapl_data_eur)
print(aapl_data_eur.dtypes)
print(aapl_data_eur.index.dtype)

# range of subsequent dates and then nalocf -> or not (and just skip nan days)? 
idx = pd.date_range("2021-06-10", datetime.now())
#aapl_data_eur.index = pd.DatetimeIndex(aapl_data_eur.index)
aapl_data_eur = aapl_data_eur.reindex(idx, method="ffill")
print(aapl_data_eur[130:140])

# An own custom plot
# plt.plot(aapl_data.index.values, aapl_data['Close'])
# plt.title('Apple Aktie')
# plt.savefig('A:\Projects\Investment-Research\plots\plot.png')

#print(aapl_data_eur.index.values)

plt.plot(aapl_data_eur.index.values, aapl_data_eur)
plt.title('Apple Aktie')
plt.savefig('A:\Projects\Investment-Research\plots\plot_eur.png')

print("END")
