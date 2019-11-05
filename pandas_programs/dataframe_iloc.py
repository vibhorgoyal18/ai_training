# Using iloc index the dataframe to print all the rows of the columns at index 3,4,5.
# Hint: Use 3,4,5 not 2,3,4

import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.iloc[:, [3, 4, 5]]
print(df_2.head(20))
