print("12-4.     20173087 노원진\n")

import pandas as pd 
df = pd.read_csv('./data/countries.csv', index_col = 0)
print(df.head())
print('\n', df.tail())
print('\n', df[3:6]) # 3, 4, 5

# pd.read_csv() 함수를 사용하여 'countries.csv' 파일에서 데이터프레임을 읽어옵니다. index_col = 0 매개변수를 사용하여 첫 번째 열을 인덱스로 설정합니다. 읽어온 데이터프레임을 df에 할당합니다.
# df.head() 함수를 사용하여 데이터프레임의 처음 5개 행을 출력합니다.
# 개행 문자 \n을 사용하여 빈 줄을 출력합니다.
# df.tail() 함수를 사용하여 데이터프레임의 마지막 5개 행을 출력합니다.
# 개행 문자 \n을 사용하여 빈 줄을 출력합니다.
# df[3:6] 코드를 사용하여 데이터프레임의 3번부터 5번까지의 행을 선택하여 출력합니다.