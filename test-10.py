# Due to an error in data entry, some rows in the 'store_info' table are duplicated. Clean the data so that there are no longer any duplicated rows.

#     store_id    type        sales
# 0   143         food        1417
# 1   143         clothing    111
# 2   143         clothing    111
# 3   419         food        6745
# 4   365         food        6745
# 5   365         food        3551

# Select the code to return the output

import pandas as pd
import numpy as np

store_info = pd.DataFrame({'store_id': [143, 143, 143, 419, 365, 365],
                            'type': ['food', 'clothing', 'clothing', 'food', 'food', 'food'],
                            'sales': [1417, 111, 111, 6745, 6745, 3551]})

store_info_no_duplicated= store_info.drop_duplicates()

print(store_info_no_duplicated)