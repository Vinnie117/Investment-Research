from openbb_terminal import api as openbb
import matplotlib.pyplot as plt 
import matplotlib
import matplotlib.rcsetup as rcsetup
from datetime import datetime

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

# Euro conversion
usdeur = openbb.forex.load(to_symbol="EUR", from_symbol="USD", resolution='d', interval='1day', start_date="2021-06-10")
usdeur_close = usdeur['Close']
print(usdeur_close)

# Convert stock price to euro
aapl_data_eur = aapl_data['Close'] * usdeur_close
print(aapl_data_eur)


# An own custom plot
plt.plot(aapl_data.index.values, aapl_data['Close'])
plt.title('Apple Aktie')
plt.savefig('A:\Projects\Investment-Research\plots\plot.png')

plt.plot(aapl_data_eur.index.values, aapl_data_eur)
plt.title('Apple Aktie')
plt.savefig('A:\Projects\Investment-Research\plots\plot_eur.png')

print("END")
