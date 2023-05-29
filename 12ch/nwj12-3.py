print("12-3.     20173087 노원진\n")
import csv
import matplotlib.pyplot as plt

f = open('./data/weather.csv','rt', encoding='UTF8')
data = csv.reader(f)
header = next(data)

monthly_wind = [ 0 for x in range(12) ]   
days_counted = [ 0 for x in range(12) ]   
for row in data: 
    month = int(row[0][5:7])              
    if row[3] !=  '' :                     
        wind = float(row[3])             
        monthly_wind[month-1] += wind 
        days_counted[month-1] += 1    
for i in range(12) :
    monthly_wind[i] /= days_counted[i]   

print(monthly_wind)
plt.bar(range(len(monthly_wind)), monthly_wind)
plt.xticks(range(0,12), range(1,13))
plt.show()
f.close()                                 

#     open() 함수를 사용하여 'weather.csv' 파일을 텍스트 모드로 엽니다.
# csv.reader() 함수를 사용하여 파일을 읽을 수 있는 CSV 리더 객체 data를 생성합니다.
# next(data)를 사용하여 첫 번째 행을 헤더로 읽어옵니다.
# monthly_wind와 days_counted 리스트를 생성합니다. monthly_wind는 월별 풍속의 합을 저장하기 위한 리스트이며, days_counted는 해당 월의 날짜 수를 저장하기 위한 리스트입니다. 초기값은 모두 0으로 설정됩니다.
# for 루프를 사용하여 데이터를 반복하면서 월별 풍속의 합과 날짜 수를 계산합니다.
# 월별 풍속의 합과 날짜 수를 이용하여 월별 평균 풍속을 계산합니다.
# 계산된 월별 평균 풍속을 출력합니다.
# plt.bar() 함수를 사용하여 막대 그래프를 생성합니다. range(len(monthly_wind))를 x축으로, monthly_wind를 y축으로 사용합니다.
# plt.xticks() 함수를 사용하여 x축 눈금을 설정합니다. 월별 숫자로 표시되도록 설정합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.
# 파일을 닫습니다.

