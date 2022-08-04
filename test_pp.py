import pandas as pd

df_xml = pd.read_xml('data\kommer.xml')
# print(df_xml)

df_depot_csv = pd.read_csv('data\Depot.csv', header=0, sep=';')
print(df_depot_csv)


df_history_csv = pd.read_csv('data\Vermögensaufstellung_-_Historie_(Standard).csv', header=0, sep=';')

df_aa_csv = pd.read_csv('data\Asset_Allocation.csv', header=0, sep=';')

df_wertpapierkonto = pd.read_csv('data\wertpapierkonto.csv', header=0, sep=';')

print('END')

