print("12-8.     20173087 노원진\n")

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('./data/weather.csv', encoding='UTF8')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather[['평균기온', 'month']].groupby('month').mean()
means['평균기온'].plot(kind='bar')
plt.title('12-8. 20173087 Noh, won jin')
plt.show()

# 코드는 pandas 라이브러리를 pd 별칭으로 가져옵니다.
# pd.read_csv() 함수를 사용하여 'UTF8' 인코딩으로 날씨 데이터를 CSV 파일에서 읽어옵니다.
# weather['일시'] 열에서 날짜 정보를 추출하기 위해 pd.DatetimeIndex() 함수를 사용합니다.
# month 열을 추가하여 월별 정보를 저장합니다.
# weather[['평균기온', 'month']].groupby('month').mean() 코드를 사용하여 '평균기온' 열과 'month' 열을 그룹화하고 월별 평균을 계산합니다.
# means['평균기온'].plot(kind='bar') 코드로 막대 그래프를 생성합니다. '평균기온' 열의 데이터를 기반으로 그래프를 그립니다.
# plt.title('12-8. 20173087 Noh, won jin') 코드를 사용하여 그래프의 제목을 설정합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.