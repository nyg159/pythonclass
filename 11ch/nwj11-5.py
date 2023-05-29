print("11-5.     20173087 노원진\n")
import numpy as np
from matplotlib import pyplot as plt

years=[1965, 1975, 1985, 1995, 2005, 2015]
ko=[130, 650, 2450, 11600, 17790, 27250]
jp=[890, 5120, 11500, 42130, 40560, 38780]
ch=[100, 200, 290, 540, 1760, 7940]

x_range=np.arange(len(years))
plt.title("GDP per capita, 20102000, 20173087, Noh won jon")
plt.ylabel("dollars")
plt.xlabel("years")
plt.bar(x_range + 0.0,ko, width=0.25)
plt.bar(x_range + 0.3,jp, width=0.25)
plt.bar(x_range +0.6,ch, width=0.25)
plt.xticks(range(len(years)), years)
plt.show()

# numpy를 np 별칭으로 가져옵니다.
# pyplot 모듈을 plt로 가져옵니다.
# 연도(years)와 각 국가(ko, jp, ch)의 GDP 데이터를 정의합니다.
# np.arange(len(years))를 사용하여 x_range 변수에 연도 수만큼의 범위를 생성합니다.
# plt.title(), plt.ylabel(), plt.xlabel() 함수를 사용하여 그래프의 제목과 축 레이블을 설정합니다.
# plt.bar() 함수를 사용하여 막대 그래프를 그립니다. 각 국가의 데이터를 x_range에 맞게 그리고, width를 조절하여 막대 간의 간격을 설정합니다.
# plt.xticks() 함수를 사용하여 x축 눈금을 설정합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.