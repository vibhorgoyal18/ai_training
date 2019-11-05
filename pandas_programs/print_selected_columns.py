# Print out the columns 'month', 'day', 'temp', 'area' from the dataframe 'df'.

import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df[['month', 'day', 'temp', 'area']]
print(df_2.head(20))
