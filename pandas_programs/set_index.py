# Using set_index command set the column 'X' as the index of the dataset and then print the head of the dataset.
# Hint: Use inplace = False

import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.set_index('X', inplace=False)
print(df_2.head())
