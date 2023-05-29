print("12-7.     20173087 노원진\n")

import pandas as pd
import matplotlib.pyplot as plt 
weather = pd.read_csv('./data/weather.csv', encoding='UTF8')
monthly = [ None for x in range(12) ]
monthly_temp = [ 0 for x in range(12) ]
weather['month'] = pd.DatetimeIndex(weather['일시']).month 

for i in range(12) :
    monthly[i] = weather[ weather['month'] == i + 1 ] 
    # old version에서 가능 # monthly_temp[i] = monthly[i].mean()['평균기온']
    monthly_temp[i] = monthly[i]['평균기온'].mean()
plt.title('12-7. 20173087 Noh, won jin')
plt.plot(monthly_temp, 'red')
plt.xticks(range(0,12), range(1,13))
plt.show()



# import pandas as pd: pandas 라이브러리를 가져옵니다. pandas는 데이터 조작 및 분석 도구를 제공합니다.

# import matplotlib.pyplot as plt: matplotlib 라이브러리에서 pyplot 모듈을 가져옵니다. pyplot은 그래프를 그리는 함수를 제공합니다.

# weather = pd.read_csv('./data/weather.csv', encoding='UTF8'): "weather.csv"라는 CSV 파일에서 날씨 데이터를 읽어와 pandas DataFrame인 weather에 저장합니다.

# monthly = [ None for x in range(12) ]: None으로 초기화된 12개 요소를 가진 monthly라는 리스트를 생성합니다.

# monthly_temp = [ 0 for x in range(12) ]: 0으로 초기화된 12개 요소를 가진 monthly_temp라는 또 다른 리스트를 생성합니다.

# weather['month'] = pd.DatetimeIndex(weather['일시']).month: weather DataFrame의 '일시' (날짜) 열에서 월을 추출하여 'month'라는 새로운 열에 할당합니다.

# for i in range(12):는 0부터 11까지 (12개월인 1월부터 12월까지를 나타냄) 반복합니다.

# monthly[i] = weather[ weather['month'] == i + 1 ]: 'month' 열이 i + 1과 동일한 조건을 만족하는 weather DataFrame의 행을 선택하고, 그 결과를 monthly[i] 리스트에 할당합니다.

# monthly_temp[i] = monthly[i]['평균기온'].mean(): monthly[i] DataFrame의 '평균기온' 열의 평균을 계산하고, 그 값을 monthly_temp[i] 리스트에 할당합니다.

# 다음 코드는 matplotlib을 사용하여 선 그래프를 생성합니다:

# plt.title('12-7. 20173087 Noh, won jin'): 그래프의 제목을 설정합니다.
# plt.plot(monthly_temp, 'red'): monthly_temp 리스트를 선 그래프로 그립니다. 색상은 빨강으로 지정합니다.
# plt.xticks(range(0,12), range(1,13)): x축의 눈금 레이블을 1부터 12까지의 숫자로 설정합니다.
# plt.show(): 그래프를 표시합니다.
# 이 코드는 'weather.csv'라는 CSV 파일이 현재 작업 디렉토리에서 'data' 폴더에 존재한다고 가정합니다.