print("12-6.     20173087 노원진\n")

import pandas as pd
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('./data/countries.csv', index_col = 0)
countries_df['density'] = countries_df['population'] / countries_df['area']
print(countries_df[0:7])

# 코드는 pandas 라이브러리를 pd 별칭으로 가져옵니다.
# pd.read_csv() 함수를 사용하여 'countries.csv' 파일에서 국가 데이터셋을 읽어옵니다. index_col = 0 매개변수를 사용하여 첫 번째 열을 인덱스로 설정합니다.
# countries_df['population'] / countries_df['area'] 코드를 사용하여 국가별 인구 밀도를 계산합니다. '인구' 열을 '면적' 열로 나누어 계산한 값을 'density' 열에 저장합니다.
# countries_df[0:7] 코드를 사용하여 데이터셋에서 첫 7개 국가의 정보를 출력합니다.