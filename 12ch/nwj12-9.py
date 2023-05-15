print("12-9.     20173087 노원진\n")

import pandas as pd

weather = pd.read_csv('./data/weather.csv', encoding='UTF8')
missing_data = weather [ weather['평균풍속'].isna() ] 
print(missing_data)

weather = pd.read_csv('./data/weather.csv', index_col = 0, encoding='UTF8')
weather.fillna(0, inplace = True) 
print()
print(weather.loc['2012-02-11'])

weather = pd.read_csv('./data/weather.csv', index_col = 0, encoding='UTF8')
weather.fillna( weather['평균풍속'].mean(), inplace = True)
print()
print(weather.loc['2012-02-11'])