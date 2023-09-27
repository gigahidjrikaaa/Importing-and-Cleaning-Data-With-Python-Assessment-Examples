import pandas as pd
import numpy as np

df = pd.DataFrame({'name': ['Heather', 'Chris', 'Eva'],
                    'height': [160.3, 175.1, 165.4]})

print(df.height.astype('int64'))