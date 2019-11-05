# Impute the mean value at all the missing values of the column 'Product_Base_Margin'
# and then print the percentage of missing values in each column.

import numpy as np
import pandas as pd

df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
df.loc[np.isnan(df['Product_Base_Margin']), ['Product_Base_Margin']] = df['Product_Base_Margin'].mean()
print(round(100 * (df.isnull().sum() / len(df.index)), 2))
