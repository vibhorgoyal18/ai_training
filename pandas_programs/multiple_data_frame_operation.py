# If all the stats are taken for both ‘ipl17’ and ‘ipl18’,
# which team with its total points greater than 25 will have the highest win percentage?

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

ipl17 = pd.DataFrame({'Team': ['MI', 'RPS', 'SRH', 'KKR', 'KXIP', 'DD', 'GL', 'RCB'],
                      'Matches': [14, 14, 14, 14, 14, 14, 14, 14],
                      'Won': [10, 9, 8, 8, 7, 6, 4, 3],
                      'Lost': [4, 5, 5, 6, 7, 8, 10, 10],
                      'Tied': [0, 0, 0, 0, 0, 0, 0, 0],
                      'N/R': [0, 0, 1, 0, 0, 0, 0, 1],
                      'Points': [20, 18, 17, 16, 14, 12, 8, 7],
                      'NRR': [0.784, 0.176, 0.469, 0.641, 0.123, -0.512, -0.412, -1.299],
                      'For': [2407, 2180, 2221, 2329, 2207, 2219, 2406, 1845],
                      'Against': [2242, 2165, 2118, 2300, 2229, 2255, 2472, 2033]},
                     index=range(1, 9)
                     )
ipl18.set_index('Team', inplace=True)
ipl17.set_index('Team', inplace=True)
ipl_17_18 = ipl18.add(ipl17, fill_value=0, )
ipl_17_18 = ipl_17_18[ipl_17_18['Points'] > 25]
ipl_17_18['win_percentage'] = 100 * (ipl_17_18['Won'] / ipl_17_18['Matches'])

print(ipl_17_18[ipl_17_18['win_percentage'] == ipl_17_18['win_percentage'].max()])
