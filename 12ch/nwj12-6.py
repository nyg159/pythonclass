print("12-6.     20173087 노원진\n")

import pandas as pd
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('./data/countries.csv', index_col = 0)
countries_df['density'] = countries_df['population'] / countries_df['area']
print(countries_df[0:7])