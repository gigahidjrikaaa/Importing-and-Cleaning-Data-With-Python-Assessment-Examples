# Expected Output:
# 0    orange
# 1    banana
# 2    orange
# 3    banana
# dtype: object

import numpy as np
import pandas as pd

data = pd.Series(['apple', 'banana', 'apple', 'banana'])
print(data.replace('apple', 'orange'))