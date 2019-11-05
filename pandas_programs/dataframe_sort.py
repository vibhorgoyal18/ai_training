# Sort the dataframe on 'month' and 'day' in ascending order in the dataframe 'df'.

import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.sort_values(by=['month', 'day'], inplace=False, ascending=True)
print(df_2.head(20))
