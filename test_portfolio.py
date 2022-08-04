from openbb_terminal import api as openbb
import matplotlib.pyplot as plt 
import matplotlib
import matplotlib.rcsetup as rcsetup
from datetime import datetime
import pandas as pd


print("START")


openbb.portfolio.load_info("Public_Equity_Orderbook.xlsx")


test = openbb.portfolio.display_orderbook(portfolio = "Public_Equity_Orderbook.xlsx")
print(test)


print("END")

