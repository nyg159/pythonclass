print("12-4.     20173087 노원진\n")

import pandas as pd 
df = pd.read_csv('./data/countries.csv', index_col = 0)
print(df.head())
print('\n', df.tail())
print('\n', df[3:6]) # 3, 4, 5