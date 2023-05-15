print("12-8.     20173087 노원진\n")

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('./data/weather.csv', encoding='UTF8')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
# old version에서 가능 # means = weather.groupby('month').mean()
means = weather[['평균기온', 'month']].groupby('month').mean()
means['평균기온'].plot(kind='bar')
plt.title('12-8. 20173087 Noh, won jin')
plt.show()
