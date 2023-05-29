print("12-10.     20173087 노원진\n")

import pandas as pd
import matplotlib.pyplot as plt
countries_df = pd.read_csv('./data/countries.csv', index_col = 0)
sorted = countries_df.sort_values('area', ascending=False)
# ascending false는 내림차순 
print(sorted[0:5])

# 코드는 필요한 라이브러리인 pandas와 matplotlib.pyplot을 가져오는 것으로 시작합니다. 이 라이브러리들은 데이터 조작과 시각화에 주로 사용됩니다.

# pd.read_csv() 함수를 사용하여 "countries.csv"라는 CSV 파일을 countries_df라는 DataFrame으로 읽어옵니다. index_col=0 인자는 CSV 파일의 첫 번째 열을 DataFrame의 인덱스 열로 설정하도록 지정합니다.

# sort_values() 메서드는 countries_df DataFrame에 호출되어 'area' 열을 기준으로 정렬합니다. ascending=False 인자는 정렬을 큰 값에서 작은 값으로 내림차순으로 수행하도록 합니다.

# 정렬된 DataFrame은 sorted라는 변수에 할당됩니다. 하지만 sorted라는 변수명은 내장된 Python sorted() 함수를 가리기 때문에 이 변수명을 사용하는 것은 좋지 않을 수 있습니다.

# 마지막으로, 코드는 슬라이싱 구문 sorted[0:5]를 사용하여 정렬된 DataFrame의 첫 다섯 개의 행을 출력합니다.