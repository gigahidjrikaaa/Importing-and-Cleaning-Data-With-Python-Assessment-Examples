# The team at Green Friends have decided to give the Kentiapalm a new nickname. Replace the name Howerd with Kenny in the 'name' column of the 'plants' DataFrame.

# --plants
#     name        binomial name           sales price
# 0   Alfredo     Monstera Deliciosa      24.95
# 1   Isabella    Calathea Orbifolia      28.95
# 2   Marty       Areca                   44.95
# 3   Ollie       Alocasia Zebrina        29.95
# 4   Howerd      Kentiapalm              49.95

# Complete the code to return the output

import pandas as pd
import numpy as np

plants = pd.DataFrame({'name': ['Alfredo', 'Isabella', 'Marty', 'Ollie', 'Howerd'],
                        'binomial name': ['Monstera Deliciosa', 'Calathea Orbifolia', 'Areca', 'Alocasia Zebrina', 'Kentiapalm'],
                        'sales price': [24.95, 28.95, 44.95, 29.95, 49.95]})

plants['name'] = plants['name'].replace('Howerd', 'Kenny')
print(plants.head())