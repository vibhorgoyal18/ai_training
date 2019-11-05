# Remove the missing values from the rows having greater than 5 missing values
# and then print the percentage of missing values in each column.

import pandas as pd

df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
df = df[df.isnull().sum(axis=1) <= 5]
print(round(100 * (df.isnull().sum() / len(df.index)), 2))
