import pandas as pd
import numpy_financial as npf
from pyxirr import xirr
from datetime import date


df_wertpapierkonto = pd.read_csv('data\wertpapierkonto.csv', header=0, sep=';', decimal=',')
print(df_wertpapierkonto.dtypes)

# Zahlenformat
df_wertpapierkonto['Wert'] = [x.replace('.', '') for x in df_wertpapierkonto['Wert']]
df_wertpapierkonto['Wert'] = [x.replace(',', '.') for x in df_wertpapierkonto['Wert']]
df_wertpapierkonto['Wert'] = df_wertpapierkonto['Wert'].astype(float)
print(df_wertpapierkonto.dtypes)

# Muss 'Wert' richtig formatieren! Als Zahl und Dezimalzeichen!
divs = df_wertpapierkonto.loc[df_wertpapierkonto['Typ'] == 'Dividende', 'Wert']
print(divs)

# 9930 ist Einkaufssumme aller WPs

# Lib um IRR zu berechnen -> stimmt mit PP überein
# https://www.youtube.com/watch?v=3L4T-UM3iqs
dates = [date(2019, 1, 1), date(2019, 7, 1), date(2020, 1, 1)]
amounts = [-50, -50, 105]

irr = xirr(dates, amounts)
print(irr)


print('END')