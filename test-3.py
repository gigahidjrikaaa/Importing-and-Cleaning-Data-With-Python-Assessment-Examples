import pandas as pd
import numpy as np

df = pd.DataFrame({'id': [7134, 4020, 6757, 2561, 6875],
                     'score': [75.0, 94.0, np.nan, 91.0, np.nan]})

print(df.fillna(80))