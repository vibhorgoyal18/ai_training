# Create a new column 'XY' which consist of values obtained from multiplying column 'X' and column 'Y'.

import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df['XY'] = df['X'] * df['Y']
print(df.head(20))
