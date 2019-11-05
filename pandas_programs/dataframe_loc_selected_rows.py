# Using loc function print out all the columns and rows from 2 to 20 of the 'df' dataset.

import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.loc[2:20]
print(df_2)
