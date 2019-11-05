# Print all the columns and the rows where 'area' is greater than 0, 'wind' is greater than 1 and the 'temp' is greater than 15.


import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.loc[(df.area > 0) & (df.wind > 1) & (df.temp > 15)]
print(df_2.head(20))
