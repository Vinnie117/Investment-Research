import pandas as pd

df_xml = pd.read_xml('data\kommer.xml')
# print(df_xml)

df_portfolio_csv = pd.read_csv('data\Depot.csv', header=0, sep=';')
print(df_portfolio_csv)


df_history_csv = pd.read_csv('data\Vermögensaufstellung_-_Historie_(Standard).csv', header=0, sep=';')


print('END')

