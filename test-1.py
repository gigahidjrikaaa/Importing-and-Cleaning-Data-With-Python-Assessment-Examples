# Consider the Pandas DataFrame "measure" below. Keep the column "Name" and convert the column "Height" to rows

#     Name    Height  Weight
# 0   Nancy   65      120
# 1   Henry    71      165
# 2   Alan     60      160
# 3   Bob    73      170

import pandas as pd

measure = pd.DataFrame({'Name': ['Nancy', 'Henry', 'Alan', 'Bob'],
                        'Height': [65, 71, 60, 73],
                        'Weight': [120, 165, 160, 170]})

print(measure)

df = pd.melt(measure, id_vars='Name', value_vars='Height')

print(df)