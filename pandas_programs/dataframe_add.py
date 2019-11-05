# Given three data frames containing the number of
# gold, silver, and bronze Olympic medals won by some countries,
# determine the total number of medals won by each country.
# Note: All the three data frames don’t have all the same countries.
# So, ensure you use the ‘fill_value’ argument (set it to zero), to avoid getting NaN values.
# Also, ensure you sort the final dataframe, according to the total medal count in descending order.


import pandas as pd

gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],
                     'Medals': [15, 13, 9]}
                    ).set_index('Country')
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],
                       'Medals': [29, 20, 16]}
                      ).set_index('Country')
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],
                       'Medals': [40, 28, 27]}
                      ).set_index('Country')

result = gold.add(silver, fill_value=0).add(bronze, fill_value=0).sort_values(by=['Medals'], ascending=False)

print(result)
