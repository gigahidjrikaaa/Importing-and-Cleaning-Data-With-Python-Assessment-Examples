# The wine data contains information on wines sold in two different stores. Some of the wines are sold in both stores, so have been duplicated in the data. Remove the rows where values in all columns are duplicated.

#     style           type    country       price       rating
# 0   malbec          red     argentina     19.04       4.2
# 1   malbec          red     argentina     18.49       4.2
# 2   alvarinho       white   portugal      18.99       4.2
# 3   riesling        white   germany       16.95       4.2
# 4   valpolicella    red     italy         19.04       4.2
# 5   valpolicella    red     italy         19.04       4.2

# Complete the code to return the output

import pandas as pd
import numpy as np

wine = pd.DataFrame({'style': ['malbec', 'malbec', 'alvarinho', 'riesling', 'valpolicella', 'valpolicella'],
                    'type': ['red', 'red', 'white', 'white', 'red', 'red'],
                    'country': ['argentina', 'argentina', 'portugal', 'germany', 'italy', 'italy'],
                    'price': [19.04, 18.49, 18.99, 16.95, 19.04, 19.04],
                    'rating': [4.2, 4.2, 4.2, 4.0, 4.2, 4.2]})

wine_no_duplicates = wine.drop_duplicates()

print(wine_no_duplicates)