# Expected Output:
# 0    False
# 1    True
# 2    False

import numpy as np
import pandas as pd

data = pd.Series([1, np.nan, 3])
print(data.isnull())