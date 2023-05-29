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
# inplace 는 정렬을 해주는것 
print()
print(weather.loc['2012-02-11'])

# # 코드는 pandas 라이브러리를 가져와 pd라는 별칭으로 사용합니다.
# pd.read_csv() 함수를 사용하여 CSV 파일에서 날씨 데이터를 읽어옵니다. encoding 매개변수는 파일 내의 UTF-8 인코딩을 처리하기 위해 'UTF8'로 설정되어 있습니다.
# missing_data 변수에는 '평균풍속' 열이 결측치인 (NaN) 행의 하위 집합이 할당됩니다.
# missing_data DataFrame을 출력하여 '평균풍속' 열이 결측값인 행을 표시합니다.
# 다음 코드 조각은 유사한 단계를 반복하지만 약간의 변형이 있습니다:
# weather DataFrame은 동일한 CSV 파일에서 다시 읽히지만, 이번에는 index_col 매개변수를 0으로 설정하여 첫 번째 열을 인덱스로 사용합니다.
# fillna() 함수를 사용하여 DataFrame의 결측값을 0으로 대체합니다. inplace=True 매개변수는 변경 사항이 weather DataFrame에 적용되도록 합니다.
# 빈 줄을 출력합니다.
# 인덱스 값이 '2012-02-11'인 weather DataFrame의 행을 출력합니다. 이는 결측값이 0으로 대체된 해당 행의 모든 열 값을 표시해야 합니다.
# weather DataFrame은 다시 CSV 파일에서 읽힙니다.
# fillna() 함수를 다시 사용하지만, 이번에는 결측값을 '평균풍속' 열의 평균값으로 대체합니다. 이로 인해 DataFrame의 결측값이 풍속의 평균값으로 대체됩니다.
# 빈 줄을 출력합니다.
# 평균값으로 결측값을 채운 weather DataFrame에서 '2012-02-11' 인덱스 값에 해당하는 행을 출력합니다. 이는 결측값이 풍속의 평균값으로 대체된 해당 행의 모든 열 값을 표시해야 합니다.
# 전반적으로, 이 코드는 날씨 데이터셋의 '평균풍속' 열의 결측값을 처리하는 다양한 방법을 보여줍니다. 첫 번째 방법은 결측값이 있는 행을 식별하고 출력하며, 두 번째 방법은 결측값을 0으로 대체하고, 세 번째 방법은 결측값을 풍속의 평균값으로