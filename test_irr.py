import pandas as pd
import numpy_financial as npf


df_wertpapierkonto = pd.read_csv('data\wertpapierkonto.csv', header=0, sep=';', decimal=',')
print(df_wertpapierkonto.dtypes)

# Zahlenformat
df_wertpapierkonto['Wert'] = [x.replace('.', '') for x in df_wertpapierkonto['Wert']]
df_wertpapierkonto['Wert'] = [x.replace(',', '.') for x in df_wertpapierkonto['Wert']]
df_wertpapierkonto['Wert'] = df_wertpapierkonto['Wert'].astype(float)
print(df_wertpapierkonto.dtypes)

# Muss 'Wert' richtig formatieren! Als Zahl und Dezimalzeichen!
divs = df_wertpapierkonto.loc[df_wertpapierkonto['Typ'] == 'Dividende', 'Wert'].sum()
print(divs)

# 9930 ist Einkaufssumme aller WPs
flows = [-9930, divs]

irr = npf.irr(flows)
print(irr)


print('END')