print("12-5.     20173087 노원진\n")

import pandas as pd
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('./data/countries.csv', index_col = 0)
#countries_df[5:10]['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm') )
countries_df[5:10]['population'].plot(kind='pie')
plt.show()

# pd.read_csv() 함수를 사용하여 'countries.csv' 파일에서 국가 데이터셋을 읽어옵니다. index_col = 0 매개변수를 사용하여 첫 번째 열을 인덱스로 설정합니다. 이를 countries_df에 할당합니다.
# countries_df[5:10]['population'] 코드를 사용하여 데이터셋에서 5번째부터 10번째까지의 국가의 'population' 열을 선택합니다.
# plot() 함수를 사용하여 선택한 국가들의 인구를 시각화합니다. 주석 처리된 코드에서는 막대 그래프로 시각화했지만, 현재 코드에서는 파이 차트로 시각화합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.
