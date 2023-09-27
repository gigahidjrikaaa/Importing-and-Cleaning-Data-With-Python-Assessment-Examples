import pandas as pd
import numpy as np

score = pd.DataFrame({'id': [101, 102, 103],
                        'math': [90.0, np.nan, 85.0],
                        'physics': [80.0, 89.0, np.nan]})

print(score.isnull())