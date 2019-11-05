# Find out the percentage of missing values in each column in the given dataset.

import pandas as pd

df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
print(round(100 * (df.isnull().sum() / len(df.index)), 2))
