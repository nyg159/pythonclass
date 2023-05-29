print("12-2.     20173087 노원진\n")
import csv
import pandas as pd
import numpy

f = open('./data/weather.csv','rt', encoding='UTF8')
data = csv.reader(f)
header = next(data)

min_temperature = 0.0

for row in data:
    if row[1] == '':
        temperature = 100
    else :
        temperature = float(row[1])

    if min_temperature > temperature:
        min_temperature = temperature


f.close()
print('지난 10년간 울릉도의 최소 온도는 {} 도'.format(min_temperature))

# open() 함수를 사용하여 'weather.csv' 파일을 텍스트 모드로 엽니다.
# csv.reader() 함수를 사용하여 파일을 읽을 수 있는 CSV 리더 객체 data를 생성합니다.
# next(data)를 사용하여 첫 번째 행을 헤더로 읽어옵니다.
# min_temperature 변수를 0.0으로 초기화합니다. 이 변수는 최소 온도를 저장하는 용도로 사용됩니다.
# for 루프를 사용하여 데이터를 반복하면서 각 행의 온도를 확인합니다.
# 온도 값이 빈 문자열인 경우에는 100을 할당합니다. 이는 온도 값이 없는 경우에 대한 처리입니다.
# 온도 값을 float() 함수를 사용하여 실수형으로 변환합니다.
# 현재까지의 최소 온도보다 작은 경우, min_temperature 변수에 현재 온도를 할당합니다.
# 파일을 닫습니다.
# 최소 온도를 출력합니다.