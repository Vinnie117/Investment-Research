from openbb_terminal import api as openbb
import matplotlib.pyplot as plt 
import matplotlib
import matplotlib.rcsetup as rcsetup

# https://stackoverflow.com/questions/7534453/matplotlib-does-not-show-my-drawings-although-i-call-pyplot-show
print(matplotlib.matplotlib_fname())
print(rcsetup.all_backends)
#matplotlib.rcParams['interactive'] == True

# https://stackoverflow.com/questions/21835847/matplotlib-show-method-does-not-open-window
# returns 'agg' -> non-interactive backend -> can only write to files!!
print(plt.get_backend())
# matplotlib.use('Agg')

# To save plots using the non-interactive backends, use the matplotlib.pyplot.savefig('filename') method.

print("START")

aapl_data = openbb.stocks.load(
    ticker="aapl",
)


candle = openbb.stocks.process_candle(aapl_data)

# The data is in here
print(type(aapl_data))
print(aapl_data)

# This is supposed to print a plot
openbb.stocks.candle("AAPL", candle, True)

# An own custom plot
plt.plot(aapl_data.index.values, aapl_data['Close'])
plt.show()


print("END")
