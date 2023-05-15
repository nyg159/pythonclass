print("12-10.     20173087 노원진\n")

import pandas as pd
import matplotlib.pyplot as plt
countries_df = pd.read_csv('./data/countries.csv', index_col = 0)
sorted = countries_df.sort_values('area', ascending=False)
print(sorted[0:5])
