# Group the data 'df' by 'month' and 'day'
# and find the mean value for column 'rain' and 'wind' using the pivot table command.


import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_1 = df.pivot_table(values=['rain', 'wind'],
                      index=['month', 'day'],
                      aggfunc='mean')
print(df_1.head(20))
