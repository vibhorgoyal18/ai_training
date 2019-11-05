# Append two datasets df_1 and df_2, and print the combined dataframe.

import warnings
import pandas as pd

warnings.filterwarnings('ignore')

df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')
df_3 = df_1.append(df_2)
print(df_3.head())
