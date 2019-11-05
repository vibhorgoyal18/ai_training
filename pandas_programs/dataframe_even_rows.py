# Print only the even numbers of rows of the dataframe 'df'.

import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df[2::2]
print(df_2.head(20))