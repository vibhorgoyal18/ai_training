# Print out the number of missing values in each column in the given dataframe.

import pandas as pd

df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
print(df.isnull().sum())
