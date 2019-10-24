# Create a series using list = [6,7,8,9,2,3,4,5] and print the output series as the square of each number in the list.
# Hint: If input series = 1,2,3 the output series should be 1,4,9
# Hint: First create the series and then using apply and lambda find the output series.

import numpy as np
import pandas as pd
series_1 = pd.Series( [6,7,8,9,2,3,4,5])
series_2 = series_1.apply(lambda x: x**2)
print(series_1)
print(series_2)