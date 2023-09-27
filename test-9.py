# Fill in the missing data with the fill value 0 in the Pandas DataFrame 'game' shown below

# game

# id      name        team
# 1       Amy         Bosses  
# 2       Bob         NaN
# 3       Chuck       NaN
# 4       Richard     Champions
# 5       Ethel       NaN
# 6       Fred        Champions
# 7       Gilly       NaN
# 8       Hank        Champions

# Complete the code to return the output

import numpy as np
import pandas as pd

game = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6, 7, 8],
                    'name': ['Amy', 'Bob', 'Chuck', 'Richard', 'Ethel', 'Fred', 'Gilly', 'Hank'],
                    'team': ['Bosses', np.nan, np.nan, 'Champions', np.nan, 'Champions', np.nan, 'Champions']})

# Print the DataFrame with the missing data filled with 0
print(game.fillna(0))