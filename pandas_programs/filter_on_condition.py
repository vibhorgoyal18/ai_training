# Suppose in ‘ipl18’, you want to filter out the teams that have an NRR greater than zero,
# and for which the ‘For’ score exceeds the ‘Against’ score, i.e. both the conditions should be satisfied.
# Which teams will be left after you perform the above filtration?

import pandas as pd

ipl18 = pd.DataFrame({'Team': ['SRH', 'CSK', 'KKR', 'RR', 'MI', 'RCB', 'KXIP', 'DD'],
                      'Matches': [14, 14, 14, 14, 14, 14, 14, 14],
                      'Won': [9, 9, 8, 7, 6, 6, 6, 5],
                      'Lost': [5, 5, 6, 7, 8, 8, 8, 9],
                      'Tied': [0, 0, 0, 0, 0, 0, 0, 0],
                      'N/R': [0, 0, 0, 0, 0, 0, 0, 0],
                      'Points': [18, 18, 16, 14, 12, 12, 12, 10],
                      'NRR': [0.284, 0.253, -0.070, -0.250, 0.317, 0.129, -0.502, -0.222],
                      'For': [2230, 2488, 2363, 2130, 2380, 2322, 2210, 2297],
                      'Against': [2193, 2433, 2425, 2141, 2282, 2383, 2259, 2304]},
                     index=range(1, 9)
                     )

print(ipl18[(ipl18['NRR'] > 0) & (ipl18['For'] > ipl18['Against'])])
