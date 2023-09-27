# Import the 'data.csv' file, shown below, as a Pandas DataFrame.

# id      name        team
# 1       Ann         Bosses
# 2       Bob         Champions
# 3       Fred        Bosses
# 4       Chuck       Champions

# Complete the code to return the output

import pandas as pd

file = 'data.csv'
df = pd.read_csv(file)

print(df)